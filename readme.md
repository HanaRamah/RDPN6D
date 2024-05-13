# RDPN6D
This repository is the official PyTorch implementation of the work:

***RDPN6D: Residual-based Dense Point-wise Network for 6Dof Object Pose Estimation Based on RGB-D Images, CVPR Workshiop DLGC, 2024***

[[Paper](https://drive.google.com/file/d/1L2YlG-hVJsCGoJVXIzRfEMh9QMBI935X/view?usp=drive_link)]

## Overview

<div align=center>
<img src="https://github.com/AI-Application-and-Integration-Lab/RDPN6D/blob/main/teaser.png" width="1600" height="800" />
</div>


## Requirements
* python==3.9.12, CUDA=12.2, requirements.txt

* Install `detectron2` from [source](https://github.com/facebookresearch/detectron2)
* `sh scripts/install_deps.sh`
* Compile the cpp extension for `farthest points sampling (fps)`:
    ```
    sh core/csrc/compile.sh
    ```

## Datasets
Download the 6D pose datasets (LM, LM-O, YCB-V) from the
[BOP website](https://bop.felk.cvut.cz/datasets/) and
[VOC 2012](https://pjreddie.com/projects/pascal-voc-dataset-mirror/)
for background images.
Please also download the `image_sets` and `test_bboxes` from
here ([BaiduNetDisk](https://pan.baidu.com/s/1gGoZGkuMYxhU9LBKxuSz0g), [OneDrive](https://1drv.ms/u/s!Ah83ZdJvIaBnnjqVy9Eyn0yxDb8i?e=0Q3qRU), password: qjfk).

The structure of `datasets` folder should look like below:
```
# recommend using soft links (ln -sf)
datasets/
├── BOP_DATASETS
    ├──lm
    ├──lmo
    ├──ycbv
├── lm_imgn  # the OpenGL rendered images for LM, 1k/obj
├── lm_renders_blender  # the Blender rendered images for LM, 10k/obj (pvnet-rendering)
├── VOCdevkit
```

* `lm_imgn` comes from [DeepIM](https://github.com/liyi14/mx-DeepIM), which can be downloaded here ([BaiduNetDisk](https://pan.baidu.com/s/1e9SJoqb0EmyqVLEVlbNQIA), [OneDrive](https://1drv.ms/u/s!Ah83ZdJvIaBnoEz5BM4Ho6_W_UUA?e=pj7Y7i), password: vr0i).

* `lm_renders_blender` comes from [pvnet-rendering](https://github.com/zju3dv/pvnet-rendering), note that we do not need the fused data.


## Training RDPN


## Evaluation
`./core/gdrn_modeling/test_gdrn.sh <config_path> <gpu_ids> <ckpt_path> (other args)`

Example:
```
./core/gdrn_modeling/test_gdrn.sh configs/gdrn/lmo/a6_cPnP_AugAAETrunc_BG0.5_lmo_real_pbr0.1_40e.py 0 output/gdrn/lmo/a6_cPnP_AugAAETrunc_BG0.5_lmo_real_pbr0.1_40e/gdrn_lmo_real_pbr.pth
```

Our trained RDPN models can be found here 
[[Linemod](https://drive.google.com/drive/folders/1-usllpw8QgoDwp9H2b8_SK05UoU347tQ?usp=sharing)][[Linemod-Occluded](https://drive.google.com/drive/folders/1h7Fb0iQ6F-hK8zf6ezo3jj5bAxTsb8In?usp=sharing)]
[[YCBV](https://drive.google.com/drive/folders/1cbxsQvUdEvS9tarLY8BYU-4wpiN1PUwH?usp=drive_link)]
[[MP6D](https://drive.google.com/drive/folders/18z28NK_lLGbRL0RIHZDR8GmVAtoaF13B?usp=sharing)]


## Result
- Evaluation result on the LineMOD dataset (ADD(-S)):
  <table class="tg">
  <thead>
    <tr>
      <th class="tg-7zrl"></th>
      <th class="tg-8d8j" colspan="3" style="text-align: center">RGB</th>
      <th class="tg-8d8j" colspan="8" style="text-align: center">RGB-D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="tg-7zrl"></td>
      <td class="tg-7zrl">PVNet</td>
      <td class="tg-7zrl">CDPN</td>
      <td class="tg-7zrl">DPODv2</td>
      <td class="tg-7zrl">PointFusion</td>
      <td class="tg-7zrl">DenseFusion(iterative)</td>
      <td class="tg-7zrl">G2L-Net</td>
      <td class="tg-2b7s">PVN3D</td>
      <td class="tg-7zrl">FFB6D</td>
      <td class="tg-7zrl">RCVPose</td>
      <td class="tg-7zrl">DFTr</td>
      <td class="tg-7zrl">RDPN6D (Ours)</td>
    </tr>
    <tr>
      <td class="tg-7zrl">MEAN</td>
      <td class="tg-7zrl">86.3 </td>
      <td class="tg-7zrl">89.9 </td>
      <td class="tg-7zrl">99.7 </td>
      <td class="tg-7zrl">73.7 </td>
      <td class="tg-7zrl">94.3 </td>
      <td class="tg-7zrl">98.7 </td>
      <td class="tg-7zrl">99.4 </td>
      <td class="tg-7zrl">99.7 </td>
      <td class="tg-7zrl">99.43 </td>
      <td class="tg-7zrl">99.8 </td>
      <td class="tg-j6zm" style="font-weight:bold">99.97</td>
    </tr>
  </tbody>
  </table>
- Evaluation result on the Linemod-Occluded dataset (ADD(-S)):
    <table class="tg">
    <thead>
        <tr>
        <th class="tg-0pky"></th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">PVN3D</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">FFB6D</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">RCVPose</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">Uni6D</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">Uni6Dv2</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">DFTr</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">RDPN6D (Ours)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td class="tg-0pky">ALL</td>
        <td class="tg-0pky">63.2</td>
        <td class="tg-0pky">66.2</td>
        <td class="tg-0pky">70.2</td>
        <td class="tg-0pky">30.7</td>
        <td class="tg-0pky">40.2</td>
        <td class="tg-0pky">77.7</td>
        <td class="tg-0pky" style="font-weight:bold">79.5</td>
        </tr>
    </tbody>
    </table>

- Evaluation result without any post refinement on the YCB-Video dataset (ADD-S AUC and ADD(-S) AUC):
  <table class="tg">
  <thead>
    <tr>
      <th class="tg-0pky"></th>
      <th class="tg-c3ow" colspan="2" style="text-align: center">PVN3D</th>
      <th class="tg-c3ow" colspan="2" style="text-align: center">FFB6D</th>
      <th class="tg-c3ow" colspan="2" style="text-align: center">RCVPose</th>
      <th class="tg-c3ow" colspan="2" style="text-align: center">ES6D</th>
      <th class="tg-c3ow" colspan="2" style="text-align: center">Uni6D</th>
      <th class="tg-c3ow" colspan="2" style="text-align: center">DFTr</th>
      <th class="tg-c3ow" colspan="2" style="text-align: center">RDPN6D (Ours)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="tg-0pky"></td>
      <td class="tg-0pky">ADDS</td>
      <td class="tg-0pky">ADD(S)</td>
      <td class="tg-0pky">ADDS</td>
      <td class="tg-0pky">ADD(S)</td>
      <td class="tg-0pky">ADDS</td>
      <td class="tg-0pky">ADD(S)</td>
      <td class="tg-0pky">ADDS</td>
      <td class="tg-0pky">ADD(S)</td>
      <td class="tg-0pky">ADDS</td>
      <td class="tg-0pky">ADD(S)</td>
      <td class="tg-0pky">ADDS</td>
      <td class="tg-0pky">ADD(S)</td>
      <td class="tg-0pky">ADDS</td>
      <td class="tg-0pky">ADD(S)</td>
    </tr>
    <tr>
      <td class="tg-0pky">ALL</td>
      <td class="tg-0pky">95.5</td>
      <td class="tg-0pky">91.8</td>
      <td class="tg-0pky">96.6</td>
      <td class="tg-0pky">92.7</td>
      <td class="tg-0pky">96.6</td>
      <td class="tg-0pky">95.2</td>
      <td class="tg-0pky">93.6</td>
      <td class="tg-0pky">89.0</td>
      <td class="tg-0pky" style="font-weight:bold">95.2</td>
      <td class="tg-0pky">88.8</td>
      <td class="tg-0pky">96.7</td>
      <td class="tg-0pky">94.4</td>
      <td class="tg-fymr" style="font-weight:bold">98.4</td>
      <td class="tg-fymr">94.6</td>
    </tr>
  </tbody>
  </table>

- Evaluation result on the MP6D dataset (ADD-S AUC):
    <table class="tg">
    <thead>
        <tr>
        <th class="tg-0pky"></th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">PVN3D</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">FFB6D</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">DFTr</th>
        <th class="tg-c3ow" colspan="1" style="text-align: center">RDPN6D (Ours)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td class="tg-0pky">ALL</td>
        <td class="tg-0pky">85.42</td>
        <td class="tg-0pky">86.29</td>
        <td class="tg-0pky">93.01</td>
        <td class="tg-0pky" style="font-weight:bold">95.9</td>
        </tr>
    </tbody>
    </table>

## Visualization
<div align=center>
<img src="https://github.com/AI-Application-and-Integration-Lab/RDPN6D/blob/main/vis.png" width="800" height="800" />
</div>

## Acknowledgment

This work can not be finished well without the following reference, many thanks for the author's contribution:

[GDR-Net](https://github.com/THU-DA-6D-Pose-Group/GDR-Net), [FFB6D](https://github.com/ethnhe/FFB6D), [MP6D](https://github.com/yhan9848/MP6D)
