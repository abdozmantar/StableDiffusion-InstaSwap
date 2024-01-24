
<div align="center">

  <img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/Logo.png?raw=true?raw=true" alt="logo" width="180px"/>

  ![Version](https://img.shields.io/badge/node_version-0.1.4-green?style=for-the-badge&labelColor=darkgreen)

  [![Commit activity](https://img.shields.io/github/commit-activity/t/abdozmantar/StableDiffusion-InstaSwap/main?cacheSeconds=0)](https://github.com/abdozmantar/StableDiffusion-InstaSwap/commits/main)
  ![Last commit](https://img.shields.io/github/last-commit/abdozmantar/StableDiffusion-InstaSwap/main?cacheSeconds=0)
  [![Opened issues](https://img.shields.io/github/issues/abdozmantar/StableDiffusion-InstaSwap?color=red)](https://github.com/abdozmantar/StableDiffusion-InstaSwap/issues?cacheSeconds=0)
  [![Closed issues](https://img.shields.io/github/issues-closed/abdozmantar/StableDiffusion-InstaSwap?color=green&cacheSeconds=0)](https://github.com/abdozmantar/comfyui-reactor-node/issues?q=is%3Aissue+is%3Aclosed)
  ![License](https://img.shields.io/github/license/abdozmantar/StableDiffusion-InstaSwap)

# InstaSwap Face Swap Extension for Stable Diffusion
</div>

### Fastest Face Swap Extension for Stable Diffusion, FastTrack: Lightning-Speed Facial Transformation for your projects.

<div align="center">

---
[**Installation**](#installation) | [**Usage**](#usage) | [**Troubleshooting**](#troubleshooting) | [**Api**](#api) | [**ComfyUI**](#comfyui) | [**Troubleshooting**](#troubleshooting) | [**Disclaimer**](#disclaimer)

---
## Demo
</div>
<div align="center">
  <img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/Demo.gif?raw=true" alt="demo" width="100%"/>
</div>

## Installation

1. If you are using Windows operating system you have to install C++ build tools for compile InsightFace library on your computer.  To do this:
   - Install [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) Communty version (skip this if you installed already)
   - Install [VS C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 
   - Open Visual Studio under `Workloads -> Desktop & Mobile` menu select `Desktop Development with C++`
   
2. Clone this repository to your Stable Diffusion extensions folder. There is three way :  

- A) Lanunch  Stable Diffusion and go to the 'Extensions' tab in the interface. Then, navigate to the Install From Url tab and enter this url to `https://github.com/abdozmantar/StableDiffusion-InstaSwap` repository text field. After entering the URL, click on the 'Install' button.
<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/extensions.jpg?raw=true" alt="webui-demo" width="100%"/>

- B) Download this repository  as a zip file and extract files in to `automatic\extensions\StableDiffusion-InstaSwap` folder.

- C) Go to `automatic\extensions\` folder open a terminal window here and run `git clone https://github.com/abdozmantar/StableDiffusion-InstaSwap` command.

3. After you clone or install StableDiffusion-InstaSwap repository in order to using it you have to restart Stable Diffusion UI.  You can click Apply and restart UI button. 
<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/restart.jpg?raw=true" alt="webui-demo" width="100%"/>
After restart you'll find InstaSwap section in the Stable Diffusion interface
<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/section.jpg?raw=true" alt="webui-demo" width="100%"/>

4. That's all! Now you can enjoy using InstaSwap!

## Usage

Using InstaSwap is as easy as child's play. All you need to do is a few clicks of the mouse. In Stable Diffusion, face swapping can be done using two different methods: Text To Image and Image To Image. Below, you can find detailed instructions on how to perform a face swap using these methods.

<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/usage.png?raw=true" alt="webui-demo" width="100%"/>

### Text To Image
In the Text to Image method, first write a detailed description of the character you want in the prompt section*(1). Continue creating images by pressing the Generate button until you get the desired result. If you have achieved the result you want, to ensure you don’t lose it, click green fixed seed button*(2) and set your seed number to text box.

<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/text2img1.jpg?raw=true" alt="webui-demo" width="100%"/>

Then, we can activate InstaSwap and setup it. Turn on the Enable checkbox *(3). Now, click on the source image panel  *(4) below and select the target face you want to change. This can be any image file.

<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/text2img2.jpg?raw=true" alt="webui-demo" width="100%"/>

Now, finally, press the Generate*(5) button again and voila! Your face swapping process is successfully completed. That's how easy it is to do a face swap with InstaSwap.

<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/text2img3.jpg?raw=true" alt="webui-demo" width="100%"/>

### Image To Image
In the Image to Image method, we aim to change the face in an already existing image. Therefore, after selecting our source image, we leave the prompt section empty without writing anything. The settings in InstaSwap are the same as in the Text to Image section above. Just enabling it and select your target face image. The important thing to note here is that to achieve the same result, we need to set the denoising strength in Stable Diffusion to a value of zero. Otherwise, the image we selected will undergo changes. After completing all the steps, press the 'Generate' button and the result will be in front of you in couple of secods !


<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/img2img.jpg?raw=true" alt="webui-demo" width="100%"/>

### Restoration
After the face swapping process, the resulting image can sometimes be of low resolution. To prevent this and achieve ultra-high-quality results, we can utilize Face Restoration model. All you need to do is select your desired restorer from the restore face panel.

<img src="https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/help/restore.jpg?raw=true" alt="webui-demo" width="100%"/>

### Gender Detection

You have the ability to designate a specific gender for detection in images. InstaSwap will only execute a face swap if the detected face fulfills this specified condition

### Face Indexes

InstaSwap identifies faces within images sequentially, starting from left to right and then from top to bottom. To target specific faces, you have the option to assign indexes to both source and input images. The indexing begins with 0 for the first face detected. You are free to arrange the indexes in your preferred sequence. For example, using 0,1,2 for the Source and 1,0,2 for the Input indicates that the face at index 1 in the Input image (the second face) will swap with the face at index 0 in the Source image (the first face), and so on.

### Api
You have the option to utilize InstaSwap either through the integrated Webui API or by using an external API. For detailed instructions, please refer to the information provided on this [page](https://github.com/abdozmantar/StableDiffusion-InstaSwap/blob/main/api.md)

## Troubleshooting

### **I. "You should at least have one model in models directory"**

Ensure that the "inswapper_128.onnx" model is located in the correct directory. It should be placed within the `stable-diffusion-webui\models\insightface` folder. If the model is located elsewhere, transfer it to this specified folder.

### **II. Any problems with installing Insightface or other dependencies**
If installation problems persist despite having VS C++ Build Tools or MS VS 2022, proceed with the following steps:
1.  Shut down your SD WebUI Server and then restart it. For users of any operating system, if the issue remains unresolved, follow these steps:
2.  If your SD WebUI Server is operational, close it.
3.  Navigate to the `venv\Lib\site-packages` directory on Windows or `venv/lib/python3.10/site-packages` on MacOS/Linux.
4.  Look for and delete any folders beginning with `~`, like `~rotobuf`.
5.  Proceed to `venv\Scripts` on Windows or `venv/bin` on MacOS/Linux.
6.  Open a Terminal or Console (cmd) in that directory and enter `activate`.
7.  First, update pip: execute `pip install -U pip`.
8.  Install the following packages one at a time:
    -   `pip install insightface==0.7.3`
    -   `pip install onnx`
    -   `pip install "onnxruntime-gpu>=1.16.1"`
    -   `pip install opencv-python`
    -   `pip install tqdm`
9.  After typing `deactivate`, you can close your Terminal or Console. Restart your SD WebUI. If ReActor still does not function correctly, please report it in the Issues section.

### **III. "TypeError: UpscaleOptions.init() got an unexpected keyword argument 'do_restore_first'"**

To address this issue, begin by deactivating all Roop-based extensions, except for the one in question:
-   Navigate to the 'Extensions -> Installed' section and deselect all Roop-based extensions apart from the relevant one.
-   Then, select 'Apply and restart UI'.

### **IV. "AttributeError: 'FaceSwapScript' object has no attribute 'enable'"**

This error is likely due to a conflict with another extension, such as "SD-CN-Animation." To resolve it:

-   Disable the "SD-CN-Animation" extension, or any other extension that might be causing the conflic

### **V. "INVALID_PROTOBUF : Load model from <...>\models\insightface\inswapper_128.onnx failed:Protobuf parsing failed" OR "AttributeError: 'NoneType' object has no attribute 'get'" OR "AttributeError: 'FaceSwapScript' object has no attribute 'save_original'"**

This issue might arise from a problem with the model file `inswapper_128.onnx`. To address this, manually download the file from the provided [link](https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx) and put it to the `stable-diffusion-webui\models\insightface` replacing existing one. Once downloaded, place it in the `stable-diffusion-webui\models\insightface` directory, replacing the existing file


### **VI. "ValueError: This ORT build has ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'] enabled" OR "ValueError: This ORT build has ['AzureExecutionProvider', 'CPUExecutionProvider'] enabled"**

To address these errors, follow these steps:
1.  Shut down your SD WebUI Server if it's currently running.
2.  In Windows, navigate to `venv\Lib\site-packages`, or on MacOS/Linux, go to `venv/lib/python3.10/site-packages`. Look for and delete any folders starting with "~", such as "~rotobuf".
3.  In Windows, open `venv\Scripts`, or on MacOS/Linux, go to `venv/bin`. Launch Terminal or Console (cmd) in this directory and type `activate`.
4.  Then execute the following commands:
    -   `python -m pip install -U pip`
    -   `pip uninstall -y onnxruntime onnxruntime-gpu onnxruntime-silicon onnxruntime-extensions`
    -   `pip install "onnxruntime-gpu>=1.16.1"`

If the problem persists, it may be due to another extension that automatically reinstalls `onnxruntime` whenever SD WebUI checks for requirements. Check your list of extensions. Some may cause `onnxruntime-gpu` to be downgraded to `onnxruntime<1.16.1` each time SD WebUI is launched. Avoid installing ORT 1.16.0 as it contains a known bug (see [GitHub Issue #17631](https://github.com/microsoft/onnxruntime/issues/17631)).

### **VII. "ImportError: cannot import name 'builder' from 'google.protobuf.internal'"**

1.  If your SD WebUI Server is operational, shut it down.
2.  Navigate to `venv\Lib\site-packages` on Windows or `venv/lib/python3.10/site-packages` on MacOS/Linux. Look for and delete any folders that begin with "~" (such as "~rotobuf").
3.  Inside the `site-packages` folder, locate the "google" folder and remove any folders within it that start with "~".
4.  Access `venv\Scripts` on Windows or `venv/bin` on MacOS/Linux, open a Terminal or Console (cmd) there, and enter `activate`.
5.  Execute the following commands:
    -   Update pip: `python -m pip install -U pip`
    -   Uninstall protobuf: `pip uninstall protobuf`
    -   Install a specific version of protobuf: `pip install "protobuf>=3.20.3"`

If these steps don't resolve the issue, it's possible that another extension is causing a conflict by installing an incompatible version of protobuf during SD WebUI's startup requirements check.


### **VIII. (For Windows users) If you still cannot build Insightface for some reasons or just don't want to install Visual Studio or VS C++ Build Tools - do the following:**

1.  If your SD WebUI Server is running, close it.
2.  Download the [prebuilt Insightface package](https://github.com/Gourieff/sd-webui-reactor/raw/main/example/insightface-0.7.3-cp310-cp310-win_amd64.whl) and place it in the root folder of stable-diffusion-webui (or SD.Next), where the "webui-user.bat" file is located, or (for A1111 Portable) where the "run.bat" file is.
3.  Open CMD in the stable-diffusion-webui (or SD.Next) root folder and execute `.\venv\Scripts\activate`, or (for A1111 Portable) simply run CMD.
4.  Update your PIP: run `python -m pip install -U pip` in the standard environment, or `system\python\python.exe -m pip install -U pip` for A1111 Portable.
5.  Install Insightface: use the command `pip install insightface-0.7.3-cp310-cp310-win_amd64.whl` for the standard setup, or `system\python\python.exe -m pip install insightface-0.7.3-cp310-cp310-win_amd64.whl` for A1111 Portable.

## ComfyUI

You can use InstaSwap with ComfyUI. For the installation instruction follow the [InstaSwap ComfyUI Node repo](https://github.com/abdozmantar/ComfyUI-InstaSwap)

## Disclaimer

This software is designed as a constructive tool in the burgeoning field of AI-generated media, aiding artists in tasks like animating custom characters or using them as models for apparel design, among others.

The creators of this software acknowledge the potential for unethical use and are dedicated to implementing measures to prevent such misuse. We are committed to developing this project in a positive direction, ensuring compliance with legal and ethical standards.

Users of this software are expected to employ it responsibly and in accordance with local laws. When using a real person's face, it is advisable to obtain their consent and to clearly label the content as a deepfake when publishing it online. The developers and contributors of this software bear no responsibility for the actions of its users.

By using this extension, you agree not to create content that:

-   Violates any laws;
-   Causes harm to individuals;
-   Disseminates harmful information or images, whether public or private;
-   Spreads misinformation;
-   Targets vulnerable groups.

This software employs the pre-trained models 'buffalo_l' and 'inswapper_128.onnx' from InsightFace, subject to the following terms:

-   According to the InsightFace license, their pre-trained models are solely for non-commercial research purposes, which applies to both auto-downloaded and manually downloaded models.

Users must strictly comply with these usage conditions. The developers and maintainers of this software are not liable for any misuse of InsightFace’s pre-trained models.

Please be aware that commercial use of this software requires you to train your own models or find commercially permissible models.

### Models Hashes

#### You can safely use models have these hashes:

inswapper_128.onnx
```
MD5:a3a155b90354160350efd66fed6b3d80
SHA256:e4a3f08c753cb72d04e10aa0f7dbe3deebbf39567d4ead6dce08e98aa49e16af
```

1k3d68.onnx

```
MD5:6fb94fcdb0055e3638bf9158e6a108f4
SHA256:df5c06b8a0c12e422b2ed8947b8869faa4105387f199c477af038aa01f9a45cc
```

2d106det.onnx

```
MD5:a3613ef9eb3662b4ef88eb90db1fcf26
SHA256:f001b856447c413801ef5c42091ed0cd516fcd21f2d6b79635b1e733a7109dbf
```

det_10g.onnx

```
MD5:4c10eef5c9e168357a16fdd580fa8371
SHA256:5838f7fe053675b1c7a08b633df49e7af5495cee0493c7dcf6697200b85b5b91
```

genderage.onnx

```
MD5:81c77ba87ab38163b0dec6b26f8e2af2
SHA256:4fde69b1c810857b88c64a335084f1c3fe8f01246c9a191b48c7bb756d6652fb
```

w600k_r50.onnx

```
MD5:80248d427976241cbd1343889ed132b3
SHA256:4c06341c33c2ca1f86781dab0e829f88ad5b64be9fba56e56bc9ebdefc619e43
```

**Please check hashsums if you download these models from unverified (or untrusted) sources**
