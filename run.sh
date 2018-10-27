JOB_NAME=test_1
BUCKET_NAME=output_0cbjlwej0u
OUTPUT_PATH=gs://$BUCKET_NAME/$JOB_NAME
REGION=us-west1
MODEL_DIR=/Users/felixmo/Desktop/artiCloud

if [[ $# -eq 0 ]]; then
	gcloud ml-engine jobs submit training $JOB_NAME \
		--job-dir $OUTPUT_PATH \
		--runtime-version 1.8 \
		--module-name trainer.task \
		--package-path trainer/ \
		--region $REGION
fi

if [[ $1 == "local" ]]; then
	gcloud ml-engine local train \
		--module-name trainer.task \
		--package-path trainer/ \
		--job-dir $MODEL_DIR
fi