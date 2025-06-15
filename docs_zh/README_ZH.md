[![SVG Banners](https://svg-banners.vercel.app/api?type=origin&text1=CosyVoice🤠&text2=文本转语音%20💖%20大语言模型&width=800&height=210)](https://github.com/Akshay090/svg-banners)

## 👉🏻 CosyVoice 👈🏻
**CosyVoice 2.0**: [演示](https://funaudiollm.github.io/cosyvoice2/); [论文](https://arxiv.org/abs/2412.10117); [Modelscope](https://www.modelscope.cn/studios/iic/CosyVoice2-0.5B); [HuggingFace](https://huggingface.co/spaces/FunAudioLLM/CosyVoice2-0.5B)

**CosyVoice 1.0**: [演示](https://fun-audio-llm.github.io); [论文](https://funaudiollm.github.io/pdf/CosyVoice_v1.pdf); [Modelscope](https://www.modelscope.cn/studios/iic/CosyVoice-300M)

## 亮点🔥

**CosyVoice 2.0** 已经发布！与1.0版本相比，新版本提供了更准确、更稳定、更快速、更优质的语音生成能力。

### 多语言支持
- **支持语言**：中文、英语、日语、韩语、中国方言（粤语、四川话、上海话、天津话、武汉话等）
- **跨语言与混合语言**：支持跨语言和代码切换场景的零样本声音克隆。

### 超低延迟
- **双向流式支持**：CosyVoice 2.0 整合了离线和流式建模技术。
- **快速首包合成**：实现低至150毫秒的延迟，同时保持高质量音频输出。

### 高精度
- **改进发音**：与CosyVoice 1.0相比，发音错误减少30%到50%。
- **基准测试成就**：在Seed-TTS评估集的困难测试集上达到最低字符错误率。

### 强稳定性
- **音色一致性**：确保零样本和跨语言语音合成的可靠声音一致性。
- **跨语言合成**：与1.0版本相比有显著改进。

### 自然体验
- **增强韵律和音质**：改进合成音频的对齐，将MOS评估分数从5.4提升到5.53。
- **情感和方言灵活性**：现在支持更细粒度的情感控制和口音调整。

## 发展路线图

- [x] 2025/05
    - [x] 添加cosyvoice 2.0 vllm支持

- [x] 2024/12
    - [x] 发布25hz cosyvoice 2.0

- [x] 2024/09
    - [x] 25hz cosyvoice基础模型
    - [x] 25hz cosyvoice声音转换模型

- [x] 2024/08
    - [x] 重复感知采样(RAS)推理用于llm稳定性
    - [x] 流式推理模式支持，包括kv缓存和sdpa用于rtf优化

- [x] 2024/07
    - [x] Flow matching训练支持
    - [x] 当ttsfrd不可用时支持WeTextProcessing
    - [x] Fastapi服务器和客户端

## 安装

### 克隆和安装

- 克隆仓库
    ``` sh
    git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
    # 如果由于网络失败无法克隆子模块，请运行以下命令直到成功
    cd CosyVoice
    git submodule update --init --recursive
    ```

- 安装Conda：请参见 https://docs.conda.io/en/latest/miniconda.html
- 创建Conda环境：

    ``` sh
    conda create -n cosyvoice -y python=3.10
    conda activate cosyvoice
    # WeTextProcessing需要pynini，使用conda安装，因为它可以在所有平台上执行。
    conda install -y -c conda-forge pynini==2.1.5
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
    
    # 如果遇到sox兼容性问题
    # ubuntu
    sudo apt-get install sox libsox-dev
    # centos
    sudo yum install sox sox-devel
    ```

### 模型下载

我们强烈建议您下载我们的预训练模型 `CosyVoice2-0.5B` `CosyVoice-300M` `CosyVoice-300M-SFT` `CosyVoice-300M-Instruct` 和 `CosyVoice-ttsfrd` 资源。

``` python
# SDK模型下载
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice2-0.5B', local_dir='pretrained_models/CosyVoice2-0.5B')
snapshot_download('iic/CosyVoice-300M', local_dir='pretrained_models/CosyVoice-300M')
snapshot_download('iic/CosyVoice-300M-SFT', local_dir='pretrained_models/CosyVoice-300M-SFT')
snapshot_download('iic/CosyVoice-300M-Instruct', local_dir='pretrained_models/CosyVoice-300M-Instruct')
snapshot_download('iic/CosyVoice-ttsfrd', local_dir='pretrained_models/CosyVoice-ttsfrd')
```

``` sh
# git模型下载，请确保已安装git lfs
mkdir -p pretrained_models
git clone https://www.modelscope.cn/iic/CosyVoice2-0.5B.git pretrained_models/CosyVoice2-0.5B
git clone https://www.modelscope.cn/iic/CosyVoice-300M.git pretrained_models/CosyVoice-300M
git clone https://www.modelscope.cn/iic/CosyVoice-300M-SFT.git pretrained_models/CosyVoice-300M-SFT
git clone https://www.modelscope.cn/iic/CosyVoice-300M-Instruct.git pretrained_models/CosyVoice-300M-Instruct
git clone https://www.modelscope.cn/iic/CosyVoice-ttsfrd.git pretrained_models/CosyVoice-ttsfrd
```

可选地，您可以解压 `ttsfrd` 资源并安装 `ttsfrd` 包以获得更好的文本标准化性能。

请注意，此步骤不是必需的。如果您不安装 `ttsfrd` 包，我们将默认使用WeTextProcessing。

``` sh
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd_dependency-0.1-py3-none-any.whl
pip install ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl
```

### 基本用法

我们强烈建议使用 `CosyVoice2-0.5B` 以获得更好的性能。
按照下面的代码了解每个模型的详细用法。

``` python
import sys
sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import CosyVoice, CosyVoice2
from cosyvoice.utils.file_utils import load_wav
import torchaudio
```

#### CosyVoice2 用法
```python
cosyvoice = CosyVoice2('pretrained_models/CosyVoice2-0.5B', load_jit=False, load_trt=False, load_vllm=False, fp16=False)

# 注意：如果你想重现 https://funaudiollm.github.io/cosyvoice2 上的结果，请在推理时添加 text_frontend=False
# 零样本用法
prompt_speech_16k = load_wav('./asset/zero_shot_prompt.wav', 16000)
for i, j in enumerate(cosyvoice.inference_zero_shot('收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。', '希望你以后能够做的比我还好呦。', prompt_speech_16k, stream=False)):
    torchaudio.save('zero_shot_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)

# 保存零样本说话人以供将来使用
assert cosyvoice.add_zero_shot_spk('希望你以后能够做的比我还好呦。', prompt_speech_16k, 'my_zero_shot_spk') is True
for i, j in enumerate(cosyvoice.inference_zero_shot('收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。', '', '', zero_shot_spk_id='my_zero_shot_spk', stream=False)):
    torchaudio.save('zero_shot_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)
cosyvoice.save_spkinfo()

# 细粒度控制，支持的控制请查看 cosyvoice/tokenizer/tokenizer.py#L248
for i, j in enumerate(cosyvoice.inference_cross_lingual('在他讲述那个荒诞故事的过程中，他突然[laughter]停下来，因为他自己也被逗笑了[laughter]。', prompt_speech_16k, stream=False)):
    torchaudio.save('fine_grained_control_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)

# 指令用法
for i, j in enumerate(cosyvoice.inference_instruct2('收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。', '用四川话说这句话', prompt_speech_16k, stream=False)):
    torchaudio.save('instruct_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)

# 双流用法，您可以使用生成器作为输入，这在使用文本llm模型作为输入时很有用
# 注意：您仍然应该有一些基本的句子分割逻辑，因为llm不能处理任意句子长度
def text_generator():
    yield '收到好友从远方寄来的生日礼物，'
    yield '那份意外的惊喜与深深的祝福'
    yield '让我心中充满了甜蜜的快乐，'
    yield '笑容如花儿般绽放。'
for i, j in enumerate(cosyvoice.inference_zero_shot(text_generator(), '希望你以后能够做的比我还好呦。', prompt_speech_16k, stream=False)):
    torchaudio.save('zero_shot_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)
```

#### CosyVoice2 vllm 用法
如果您想使用vllm进行推理，请安装 `vllm==v0.9.0`。较旧的vllm版本不支持CosyVoice2推理。

请注意，`vllm==v0.9.0` 有很多特定要求，例如 `torch==2.7.0`。您可以创建一个新环境，以防您的硬件不支持vllm且旧环境损坏。

``` sh
conda create -n cosyvoice_vllm --clone cosyvoice
conda activate cosyvoice_vllm
pip install vllm==v0.9.0 -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
python vllm_example.py
```

#### CosyVoice 用法
```python
cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-SFT', load_jit=False, load_trt=False, fp16=False)
# sft用法
print(cosyvoice.list_available_spks())
# 将stream=True改为块流推理
for i, j in enumerate(cosyvoice.inference_sft('你好，我是通义生成式语音大模型，请问有什么可以帮您的吗？', '中文女', stream=False)):
    torchaudio.save('sft_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M')
# 零样本用法，<|zh|><|en|><|jp|><|yue|><|ko|> 分别表示中文/英语/日语/粤语/韩语
prompt_speech_16k = load_wav('./asset/zero_shot_prompt.wav', 16000)
for i, j in enumerate(cosyvoice.inference_zero_shot('收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。', '希望你以后能够做的比我还好呦。', prompt_speech_16k, stream=False)):
    torchaudio.save('zero_shot_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)
# 跨语言用法
prompt_speech_16k = load_wav('./asset/cross_lingual_prompt.wav', 16000)
for i, j in enumerate(cosyvoice.inference_cross_lingual('<|en|>And then later on, fully acquiring that company. So keeping management in line, interest in line with the asset that\'s coming into the family is a reason why sometimes we don\'t buy the whole thing.', prompt_speech_16k, stream=False)):
    torchaudio.save('cross_lingual_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)
# 语音转换用法
prompt_speech_16k = load_wav('./asset/zero_shot_prompt.wav', 16000)
source_speech_16k = load_wav('./asset/cross_lingual_prompt.wav', 16000)
for i, j in enumerate(cosyvoice.inference_vc(source_speech_16k, prompt_speech_16k, stream=False)):
    torchaudio.save('vc_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-Instruct')
# 指令用法，支持 <laughter></laughter><strong></strong>[laughter][breath]
for i, j in enumerate(cosyvoice.inference_instruct('在面对挑战时，他展现了非凡的<strong>勇气</strong>与<strong>智慧</strong>。', '中文男', 'Theo \'Crimson\', is a fiery, passionate rebel leader. Fights with fervor for justice, but struggles with impulsiveness.', stream=False)):
    torchaudio.save('instruct_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)
```

#### 启动网页演示

您可以使用我们的网页演示页面快速上手CosyVoice。

有关详细信息，请参见演示网站。

``` python
# 将iic/CosyVoice-300M-SFT改为sft推理，或将iic/CosyVoice-300M-Instruct改为指令推理
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M
```

#### 高级用法

对于高级用户，我们在 `examples/libritts/cosyvoice/run.sh` 中提供了训练和推理脚本。

#### 构建用于部署

可选地，如果您想要服务部署，
您可以运行以下步骤。

``` sh
cd runtime/python
docker build -t cosyvoice:v1.0 .
# 如果要使用指令推理，请将iic/CosyVoice-300M更改为iic/CosyVoice-300M-Instruct
# grpc用法
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/grpc && python3 server.py --port 50000 --max_conc 4 --model_dir iic/CosyVoice-300M && sleep infinity"
cd grpc && python3 client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
# fastapi用法
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/fastapi && python3 server.py --port 50000 --model_dir iic/CosyVoice-300M && sleep infinity"
cd fastapi && python3 client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
```

## 讨论与交流

您可以直接在 [Github Issues](https://github.com/FunAudioLLM/CosyVoice/issues) 上讨论。

您也可以扫描二维码加入我们的官方钉钉聊天群。

<img src="./asset/dingding.png" width="250px">

## 致谢

1. 我们从 [FunASR](https://github.com/modelscope/FunASR) 借用了大量代码。
2. 我们从 [FunCodec](https://github.com/modelscope/FunCodec) 借用了大量代码。
3. 我们从 [Matcha-TTS](https://github.com/shivammehta25/Matcha-TTS) 借用了大量代码。
4. 我们从 [AcademiCodec](https://github.com/yangdongchao/AcademiCodec) 借用了大量代码。
5. 我们从 [WeNet](https://github.com/wenet-e2e/wenet) 借用了大量代码。

## 免责声明
上述内容仅供学术目的，旨在展示技术能力。一些示例来源于互联网。如有任何内容侵犯您的权利，请联系我们要求删除。 