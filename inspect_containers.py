import docker
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("docker_error.log"), logging.StreamHandler()],
)

def handle_container_config(container_id):
    """
    Check for the 'ContainerConfig' key in the container's attributes and handle errors gracefully.
    """
    try:
        # Initialize Docker client
        client = docker.from_env()

        # Get container details
        container = client.containers.get(container_id)
        container_attrs = container.attrs

        # Check for 'ContainerConfig'
        if 'ContainerConfig' in container_attrs:
            logging.info(f"'ContainerConfig' found for container {container_id}.")
            logging.info(f"ContainerConfig: {container_attrs['ContainerConfig']}")
        else:
            logging.warning(f"'ContainerConfig' key is missing for container {container_id}.")
            # Handle the missing key scenario (custom logic can be added here)
            logging.info(f"Available keys: {list(container_attrs.keys())}")

    except docker.errors.NotFound:
        logging.error(f"Container with ID '{container_id}' not found.")
    except docker.errors.APIError as api_error:
        logging.error(f"API error occurred: {api_error}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def list_and_handle_containers():
    """
    List all containers and handle their 'ContainerConfig' attributes.
    """
    try:
        # Initialize Docker client
        client = docker.from_env()

        # List all containers
        containers = client.containers.list(all=True)
        if not containers:
            logging.info("No containers found.")
            return

        # Iterate through each container and check 'ContainerConfig'
        for container in containers:
            logging.info(f"Processing container: {container.id}")
            handle_container_config(container.id)

    except docker.errors.APIError as api_error:
        logging.error(f"API error occurred: {api_error}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    logging.info("Starting Docker container inspection automation...")
    list_and_handle_containers()

