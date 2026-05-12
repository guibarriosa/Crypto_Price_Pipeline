# Here we define an EventBridge rule that triggers every 10 minutes
resource "aws_cloudwatch_event_rule" "crypto_lambda_schedule" {
  name                = "crypto-lambda-schedule"
  description         = "Trigger crypto pipeline every 10 minutes"
  schedule_expression = "rate(10 minutes)"
}

# Here we link the EventBridge rule to the Lambda function
resource "aws_cloudwatch_event_target" "crypto_lambda_target" {
  rule      = aws_cloudwatch_event_rule.crypto_lambda_schedule.name
  target_id = "CryptoPipelineLambda"
  arn       = aws_lambda_function.crypto_pipeline.arn
}

# Here we give EventBridge permission to invoke the Lambda function
resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.crypto_pipeline.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.crypto_lambda_schedule.arn
}