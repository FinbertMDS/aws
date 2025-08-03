docker run -it \
  ghcr.io/thatonecodes/examtopics-downloader:latest \
  -p amazon -s aws-certified-solutions-architect-professional-sap-c02 \
  -save-links -o aws-sap-c02-new.md
docker cp nervous_mestorf:/app/aws-sap-c02-new.md .
docker cp nervous_mestorf:/app/saved-links.txt .
docker rm nervous_mestorf
