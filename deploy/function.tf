resource "aws_iam_role" "iam_for_lambda" {
  name = "${var.project}-lambda-sshkeygen-generator"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "function.zip"
  function_name = "${var.project}-ssh-key-generator"
  role          = "${aws_iam_role.iam_for_lambda.arn}"
  handler       = "lambda_function.lambda_handler"

  source_code_hash = "${filebase64sha256("${var.function_path}")}"

  runtime = "python3.7"

  environment {
    variables = {
      CONFIG_BUCKET = "emirdaas-bucket"
    }
  }
}