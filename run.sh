MODEL_DIR=/Users/felixmo/Desktop/artiCloud

gcloud ml-engine local train \
    --module-name trainer.task \
    --package-path trainer/ \
    --job-dir $MODEL_DIR