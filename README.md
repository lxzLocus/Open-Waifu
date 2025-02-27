# Open-Waifu

## Abstruct

character chat bot with stable diffusion

Text-generation-webuiとstable diffusionを利用したキャラクターチャットボットのバックエンドの実現


## Start Docker

`docker compose up -d`

1. 事前にビルドをする

`dockercompose--profiledownloadup--build`

2. 起動する

`docker compose --profile auto up --build`



`./services/text-generation-webui/config/models`にLLMモデルを配置する．

## ポート

- メイン（TypeScriptホスト） : 未定
- Text-generation-webui ：7865
- AUTOMATIC1111：7870
