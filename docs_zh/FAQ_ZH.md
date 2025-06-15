# 常见问题

## ModuleNotFoundError: No module named 'matcha'

Matcha-TTS是一个第三方模块。请检查 `third_party` 目录。如果没有 `Matcha-TTS`，请执行 `git submodule update --init --recursive`。

如果您想在python脚本中使用 `from cosyvoice.cli.cosyvoice import CosyVoice`，请运行 `export PYTHONPATH=third_party/Matcha-TTS`。

## 找不到resource.zip或无法解压resource.zip

请确保您已安装git-lfs。执行以下命令：

```sh
git clone https://www.modelscope.cn/iic/CosyVoice-ttsfrd.git pretrained_models/CosyVoice-ttsfrd
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd-0.3.6-cp38-cp38-linux_x86_64.whl
``` 