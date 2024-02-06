resource "aws_instance" "new-instance" {
    ami = var.AMIS[var.REGION]
    instance_type = "t2.micro"
    availability_zone = var.ZONE1
    key name = "enter kewy name here"
    vpc_security_group_ids = ["enter security group id here"]
    tags = {
        Name = "new-instance"
        # Enter whatever tag you need to identify this instance
    }
}