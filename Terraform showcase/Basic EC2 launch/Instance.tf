provider "aws {
    region = " enter region"
    
    # For best practices it is not advsable to enter keys here especiall if this file is going to be stored in a a public repo
    access_key = "enter access_key"
    secret key = "enter secret key"
}

resource "aws_instance" "intro" {
    ami = "ami-03657b56516ab7912"
    instance_tpe = "t2.micro"
    availability_zone = " enter availability zone here"
    key_name = "enter key name"
    vpc_security_group_ids = ["security group id"]
    tags = {
        Name = "enter what you want to name instance here"
    }
}
