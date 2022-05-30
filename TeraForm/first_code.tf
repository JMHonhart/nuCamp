provider "aws" {
  profile = "default"
  region  = "US-WEST-2"
}

resource "aws_s3_bucket" "tf_course" {
  bucket = "tf_course-20220419"
  acl    = "private"
}
