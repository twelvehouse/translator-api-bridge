# translator-api-bridge
An API bridge to convert POST-based translation API requests into GET, designed for use with xUnity.AutoTranslator.

## How to Use
After cloning the repository, create a `.env` file in the same directory as `main.py` and define the following environment variables:
```
API_URL=<URL of the translation API. If you're running the DeepLX API server on the same machine, use http://localhost:1188/translate>
HOST=<The host URL where this API bridge will run. Default is 127.0.0.1>
PORT=<The port to listen on. Default is 5000>
TARGET_LANG=<The target language for translation. For Japanese, set it to ja>
```
