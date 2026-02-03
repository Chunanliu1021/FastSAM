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
```
2. Usage
Real-time & Video Inference
Inference_d435.py: Real-time segmentation via Intel RealSense D435.

inference_video.py: Video stream processing.

Inference_d435_without_overlap.py: Modified for multi-topic handling to prevent mask overlapping.

3. Masking & Depth Processing
prompt_backup.py: Primary method using both depth data and depth masks for segmentation.

rgb_limit_depth.py: Filters RGB data based on depth constraints. Located in /catkin_ws/src/test_pkg/scripts.

prompt_0116_backup.py: Archive of alternative masking methods with lower accuracy.
