resource "aws_instance" "intro" {
    ami = var.AMIS[var.REGION]
    instance_type = "t2.micro"
}