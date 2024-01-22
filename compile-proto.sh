# Root directory of app
ROOT_DIR=$(git rev-parse --show-toplevel)

# Path to Protoc Plugin
PROTOC_GEN_TS_PATH="${ROOT_DIR}/node_modules/.bin/ts-protoc-gen"

# Directory holding all .proto files
SRC_DIR="${ROOT_DIR}/protos/raw"

# Directory to write generated code (.d.ts files)
OUT_DIR="${ROOT_DIR}/protos/gen"

# Clean all existing generated files
rm -r "${OUT_DIR}"
mkdir "${OUT_DIR}"

# Generate all messages
protoc \
    --proto_path="${SRC_DIR}" $(find "${SRC_DIR}" -name "*.proto") \
    --plugin=ts-protoc-gen="${PROTOC_GEN_TS_PATH}" \
    --ts_out=service=grpc-node:"${OUT_DIR}"