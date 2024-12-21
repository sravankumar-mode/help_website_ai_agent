# Docker Usage for Help_AI_AGENT

This README provides instructions on how to use the **Help_AI_AGENT** Docker image.

## Docker Image Usage

To run the **Help_AI_AGENT** application using Docker, follow these steps:

1. **Pull the Docker Image**:

   First, pull the latest version of the Docker image:

   ```bash
   docker pull sravanmode/help-agent:latest

2. **Run the Docker Container**:

  Once the image is pulled, you can run the Docker container with the following command:
  
   ```bash
  docker run -it --rm help-agent --url https://help.zluri.com/
   ```

   This command will run the main.py script inside the container.

   Replace https://help.zluri.com/ with the desired URL you want to scrape or analyze.
  
   The --rm flag ensures the container is removed after execution, and the -it flag allows interactive terminal access.

For detailed information on how to understand and run the code, please refer to the README file inside the Help_AI_AGENT folder.
