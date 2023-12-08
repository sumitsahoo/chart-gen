##########################################################################################
# Builder image
##########################################################################################
# Using python debian slim version
FROM python:3.12-slim AS builder-image

# Update and install dependencies
RUN apt-get update -y \
    && apt-get install --no-install-recommends -y gcc python3-dev \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
# Using final folder name to avoid path issues with packages
RUN python3.12 -m venv /home/appuser/venv
ENV PATH="/home/appuser/venv/bin:$PATH"

# Install python dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt


##########################################################################################
# Runner image
##########################################################################################
# Using python debian slim version
FROM python:3.12-slim AS runner-image

# Update and install dependencies
RUN apt-get update -y \
    && apt-get upgrade -y \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user appuser with home directory
RUN set -ex \
    # Create a non-root user
    && addgroup --system --gid 1001 appgroup \
    && adduser --system --uid 1001 --gid 1001 appuser --home /home/appuser

# Create app directory and copy virtual environment from builder image
RUN mkdir /home/appuser/app
COPY --from=builder-image /home/appuser/venv /home/appuser/venv

# Set the working directory to app directory and copy source files
WORKDIR /home/appuser/app
COPY . .

# Give ownership of app directory to appuser
RUN chown -R appuser:appgroup /home/appuser/app

ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1

# Set python virtual environment path and add it to PATH
ENV VIRTUAL_ENV=/home/appuser/venv
ENV PATH="/home/appuser/venv/bin:$PATH"

EXPOSE 8080
CMD ["python3", "main.py"]

# Set the user to run the application as non root
USER appuser
