> 说明：该fork记录本人在macOS下的部署运行细节
> - 系统环境：
>   - OS: macOS Ventura 版本13.4.1(c)
>   - 硬件：Apple M2 Max，12CPU，64GB内存
> - 运行效果：
>   - 比较耗内存和CPU，期间CPU温度最高能达到80+摄氏度
>     - 建议这个过程中不要再运行其他高消耗的应用，否则电脑很容易卡死
>   - 180页左右的漫画耗时1小时左右
> - 翻译效果：
>   - 差强人意，不过聊胜于无

# MacOS环境下部署运行细节

## 运行方式实践
- ❌App打包签名失败
- ✅Python虚拟环境方式部署 + 运行
  - 原文档中对环境的部署这块交代的不够清楚，需要自己查漏补缺
    - Python虚拟环境的搭建 （见👇部署细节）
    - 依赖库的缺失&版本 （已更新requirements_macOS.txt）

## 环境部署

```shell
# 克隆仓库
git clone https://github.com/typemegan/BallonsTranslator.git 
cd BallonsTranslator

# 安装 pyenv
brew install pyenv mecab  

# 安装虚拟环境管理工具
pip3 install virtualenv

# 安装指定python版本 （有些库要3.9版本才支持）
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.9.13

# 在当前目录指定python版本
pyenv local 3.9.13   # 会产生文件.python-version，记录版本信息

# 在当前目录创建虚拟环境
pyenv exec python -m venv env  # 产生env目录，里面有虚拟环境的所有信息

# 进入虚拟环境
source env/bin/activate

# 安装依赖, macOS安装requirements_macOS.txt
pip install -r requirements_macOS.txt

# 如果需要退出虚拟环境：
deactivate
```
> 💡期间如有失败，根据失败信息谷歌自行解决

## 下载AI翻译模型并与原data目录进行合并
- 从 [MEGA](https://mega.nz/folder/gmhmACoD#dkVlZ2nphOkU5-2ACb5dKw) or [Google Drive](https://drive.google.com/drive/folders/1uElIYRLNakJj-YS0Kd3r3HE-wzeEvrWd?usp=sharing) 下载**data**文件夹并拖拽到 ```BallonsTranslator/ballontranslator```目录下
- 弹出确认选择合并"data目录"
> ⚠️注意是合并而不是替换

## 运行
```shell
# 进入👆的目录
cd BallonsTranslator

# 激活虚拟环境
source env/bin/activate

# 运行程序
python ballontranslator
```
- 之后会起来一个窗口界面，所有的操作就可以基于这个界面进行了
  - 打开漫画图片所在目录
  - 点击"Run"
- 注意：涉及到谷歌翻译，国内环境需要搭梯子
  - 建议界面设置里把超时延长一些
- 注意：不同于APP运行方式，这种运行方式要中断的话需要"强制退出" （不了解的谷歌"Mac强制退出进程"）
  - 期间报错的话也不会自动退出（比如网络超时），此时也需要"强制退出"
- 注意：运行不会断点继续
  - 中断之后再运行的话程序会重新将所有的图片跑一遍，为了避免这个重复过程：
    - 可以将跑出的结果的图片挪出操作目录 (可以写个脚本操作：比照result目录挪走已翻译的图片)
    - 另外无法翻译的图片（比如误识别图片字符超过5000异常的）也需要将图片挪出操作目录，否则无法进行下去




---

# BallonTranslator
简体中文 | [English](README_EN.md) | [Русский](README_RU.md) | [日本語](README_JA.md) | [Indonesia](README_ID.md)

深度学习辅助漫画翻译工具, 支持一键机翻和简单的图像/文本编辑  

<img src="doc/src/ui0.jpg" div align=center>

<p align=center>
界面预览
</p>

# Features
* 一键机翻  
  - 译文回填参考对原文排版的估计, 包括颜色, 轮廓, 角度, 朝向, 对齐方式等
  - 最后效果取决于文本检测, 识别, 抹字, 机翻四个模块的整体表现  
  - 支持日漫和美漫
  - 英译中, 日译英排版已优化, 文本布局以提取到的背景泡为参考, 中文基于pkuseg进行断句, 日译中竖排待改善
  
* 图像编辑  
  支持掩膜编辑和修复画笔
  
* 文本编辑  
  - 支持所见即所得地富文本编辑和一些基础排版格式调整、字体样式预设
  - 支持全文/源文/译文查找替换
  - 支持导入导出word文档

* 适用于条漫

# 使用说明

### 发布版

Windows用户可从[MEGA](https://mega.nz/folder/gmhmACoD#dkVlZ2nphOkU5-2ACb5dKw) or [Google Drive](https://drive.google.com/drive/folders/1uElIYRLNakJj-YS0Kd3r3HE-wzeEvrWd?usp=sharing)(注意: 需要从github release 下载最新版Ballonstranslator-1.3.xx, 解压并覆盖到**Ballontranslator-1.3.0-core**或者较旧的安装目录以更新程序.)

### 运行源码 (jiyu)

```bash
# 克隆仓库
$ git clone https://github.com/dmMaze/BallonsTranslator.git ; cd BallonsTranslator

# 安装依赖, macOS安装requirements_macOS.txt
$ pip install -r requirements.txt
```

如果有N卡可以安装torch-cuda启用GPU加速: 

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu116
```

从 [MEGA](https://mega.nz/folder/gmhmACoD#dkVlZ2nphOkU5-2ACb5dKw) or [Google Drive](https://drive.google.com/drive/folders/1uElIYRLNakJj-YS0Kd3r3HE-wzeEvrWd?usp=sharing) 下载**data**文件夹并移动到 ```BallonsTranslator/ballontranslator```目录, 最后运行
```bash
python ballontranslator
```

如果要使用Sugoi翻译器(仅日译英), 下载[离线模型](https://drive.google.com/drive/folders/1KnDlfUM9zbnYFTo6iCbnBaBKabXfnVJm), 将 "sugoi_translator" 移入BallonsTranslator/ballontranslator/data/models.  

### Apple Silicon Mac 本地构建.app应用
```
# 安装Python 3.9.13虚拟环境
brew install pyenv mecab
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.9.13
pyenv global 3.9.13
python3 -m venv ballonstranslator
source ballonstranslator/bin/activate

# 克隆仓库
git clone https://github.com/dmMaze/BallonsTranslator.git
cd BallonsTranslator

# 安装依赖
pip3 install -r requirements_macOS.txt

# 打包应用
cd ballontranslator
sudo pyinstaller __main__.spec

# 打包好的`BallonsTranslator.app`在`dist`文件夹下
# 需要注意的是，现在的应用还无法使用，需要到 [MEGA](https://mega.nz/folder/gmhmACoD#dkVlZ2nphOkU5-2ACb5dKw) 或者 [Google Drive](https://drive.google.com/drive/folders/1uElIYRLNakJj-YS0Kd3r3HE-wzeEvrWd?usp=sharing) 下载`data`并覆盖到`BallonsTranslator.app/Contents/Resources/data`, 覆盖的时候选择“合并”，覆盖完成后应用最终打包完整，开箱即用，将应用拖到macOS的应用程序文件夹即可，不需要再配置Python环境。
```

## 一键翻译
**建议在命令行终端下运行程序**, 首次运行请先配置好源语言/目标语言, 打开一个带图片的文件夹, 点击Run等待翻译完成  
<img src="doc/src/run.gif">  

一键机翻嵌字格式如大小、颜色等默认是由程序决定的, 可以在设置面板->嵌字菜单中改用全局设置. 全局字体格式就是未编辑任何文本块时右侧字体面板显示的格式:  
<img src="doc/src/global_font_format.png"> 

## 画板

## 修复画笔
<img src="doc/src/imgedit_inpaint.gif">
<p align = "center">
修复画笔
</p>

### 矩形工具
<img src="doc/src/rect_tool.gif">
<p align = "center">
矩形工具
</p>

按下鼠标左键拖动矩形框抹除框内文字, 按下右键拉框清除框内修复结果.  
抹除结果取决于算法(gif中的"方法1"和"方法2")对文字区域估算的准确程度, 一般拉的框最好稍大于需要抹除的文本块. 两种方法都比较玄学, 能够应付绝大多数简单文字简单背景, 部分复杂背景简单文字/简单背景复杂文字, 少数复杂背景复杂文字, 可以多拉几次试试.  
勾选"自动"拉完框立即修复, 否则需要按下"修复"或者空格键才进行修复, 或"Ctrl+D"删除矩形选框.  

## 文本编辑
<img src="doc/src/textedit.gif">


<p align = "center">
文本编辑
</p>

<img src="doc/src/multisel_autolayout.gif" div align=center>
<p align=center>
批量文本格式调整及自动排版
</p>

<img src="doc/src/ocrselected.gif" div align=center>
<p align=center>
OCR并翻译选中文本框
</p>

## 界面说明及快捷键
* Ctrl+Z, Ctrl+Y可以撤销重做大部分操作，注意翻页后撤消重做栈会清空
* A/D或pageUp/Down翻页, 如果当前页面未保存会自动保存
* "T"切换到文本编辑模式下(底部最右"T"图标), W激活文本块创建模式后在画布右键拉文本框
* "P"切换到画板模式, 右下角滑条改原图透明度
* 底部左侧"OCR"和"A"按钮控制启用/禁用OCR翻译功能, 禁用后再Run程序就只做文本检测和抹字  
* 设置面板配置各自动化模块参数
* Ctrl++/-或滚轮缩放画布
* Ctrl+A可选中界面中所有文本块
* Ctrl+F查找当前页, Ctrl+G全局查找

<img src="doc/src/configpanel.png">  

# 自动化模块
本项目重度依赖[manga-image-translator](https://github.com/zyddnys/manga-image-translator), 在线服务器和模型训练需要费用, 有条件请考虑支持一下
- Ko-fi: <https://ko-fi.com/voilelabs>
- Patreon: <https://www.patreon.com/voilelabs>
- 爱发电: <https://afdian.net/@voilelabs>

Sugoi翻译器作者: [mingshiba](https://www.patreon.com/mingshiba).
  
### 文本检测
暂时仅支持日文(方块字都差不多)和英文检测, 训练代码和说明见https://github.com/dmMaze/comic-text-detector

### OCR
 * mit_32px模型来自manga-image-translator, 支持日英汉识别和颜色提取
 * mit48px_ctc模型来自manga-image-translator, 支持日英汉韩语识别和颜色提取
 * [manga_ocr](https://github.com/kha-white/manga-ocr)来自[kha-white](https://github.com/kha-white), 支持日语识别, 注意选用该模型程序不会提取颜色

### 图像修复
  * AOT修复模型来自manga-image-translator
  * patchmatch是非深度学习算法, 也是PS修复画笔背后的算法, 实现来自[PyPatchMatch](https://github.com/vacancy/PyPatchMatch), 本程序用的是我的[修改版](https://github.com/dmMaze/PyPatchMatchInpaint)
  

### 翻译器

 * <s>谷歌翻译能挂代理建议把url从cn改成com</s> 谷歌翻译器已经关闭中国服务, 大陆再用需要设置全局代理, 并在设置面板把url换成*.com
 * 彩云, 需要申请[token](https://dashboard.caiyunapp.com/)
 * papago  
 * DeepL 和 Sugoi(及它的CT2 Translation转换)翻译器, 感谢[Snowad14](https://github.com/Snowad14)  

 如需添加新的翻译器请参考[加别的翻译器](doc/加别的翻译器.md), 本程序添加新翻译器只需要继承基类实现两个接口即可不需要理会代码其他部分, 欢迎大佬提pr

## 杂
* 如果电脑带N卡, 程序默认对所有模型启用GPU加速, 默认配置下显存占用在6G左右. 4G显存调小修复器inpaint_size即可.  
* 感谢[bropines](https://github.com/bropines)提供俄语翻译
* 第三方输入法可能会造成右侧编辑框显示bug, 见[#76](https://github.com/dmMaze/BallonsTranslator/issues/76), 暂时不打算修
* 选中文本迷你菜单支持*聚合词典专业划词翻译*[沙拉查词](https://saladict.crimx.com): [安装说明](doc/saladict_chs.md)

## 一键翻译结果预览
|            Original            |         Translated (CHS)         |         Translated (ENG)         |
| :-----------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: |
|![Original](ballontranslator/data/testpacks/manga/original2.jpg 'https://twitter.com/mmd_96yuki/status/1320122899005460481')| ![Translated (CHS)](doc/src/result2.png) | ![Translated (ENG)](doc/src/original2_eng.png) |
|![Original](ballontranslator/data/testpacks/manga/original3.jpg 'https://twitter.com/_taroshin_/status/1231099378779082754')| ![Translated (CHS)](doc/src/original3.png) | ![Translated (ENG)](doc/src/original3_eng.png) |
| ![Original](ballontranslator/data//testpacks/manga/AisazuNihaIrarenai-003.jpg) | ![Translated (CHS)](doc/src/AisazuNihaIrarenai-003.png) | ![Translated (ENG)](doc/src/AisazuNihaIrarenai-003_eng.png) |
|           ![Original](ballontranslator/data//testpacks/comics/006049.jpg)           | ![Translated (CHS)](doc/src/006049.png) | |