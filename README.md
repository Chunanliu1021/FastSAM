# FastSAM Implementation for Robotic Vision

This repository contains implementations and utility scripts for FastSAM (Fast Segment Anything Model), specifically for robotic applications using Intel RealSense D435 and depth-based segmentation.

## 1. Environment Setup

The project runs within a Docker container to ensure environment consistency.

### Start Docker Environment
```bash
# Initialize the Docker environment
source ~/NCTU/docker/FastSAM_docker/docker/docker_start.sh

# Navigate to the workspace
cd ~/FastSAM_docker/FastSAM
