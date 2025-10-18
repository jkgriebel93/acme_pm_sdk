#!/usr/bin/env bash
set -euo pipefail

# Configurable values
DOMAIN="my-domain"
REPOSITORY="python-repo"
REGION="us-west-2"
ACCOUNT_ID="123456789012"

# Authenticate with CodeArtifact
echo "🔐 Logging in to AWS CodeArtifact..."
aws codeartifact login \
  --tool twine \
  --domain "$DOMAIN" \
  --domain-owner "$ACCOUNT_ID" \
  --repository "$REPOSITORY" \
  --region "$REGION"

# Build the package using uv
echo "📦 Building the package..."
uv build

# Upload to CodeArtifact using twine
echo "🚀 Uploading to CodeArtifact..."
twine upload --repository codeartifact dist/*

echo "✅ Publish complete!"
