# Use the official Nginx base image
FROM nginx:latest

# Expose port 80 for incoming traffic
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
