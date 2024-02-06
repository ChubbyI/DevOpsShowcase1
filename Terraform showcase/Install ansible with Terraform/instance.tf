resource "aws_key_pair" "example-key: {
    key_name = "instert key name here"
    public_key = file("examplekey.pub")
}

resource "aws_instance" "test-inst" {
    ami = var.AMIS[var.REGION]
    instance_type = "t2.micro"
    availability_zone = var.ZONE1
    key_name = aws_key_pair.example-key.key_name
    vpc_security_group_ids = ["enter security group id here"]
    tags = {
        Name = "new-instance"
        # Enter whatever tag you need to identify this instance
    }

    provisioner "file" {
        source = "ansible.sh"
        destination = "/tmp/ansible.sh"
    }

    provisioner "remote-exec" {

        inline = [
            "chmod u+x /tmp/ansible.sh"
            "sudo /tmp/web.sh"
        ]
    }

    connection {
        user = var.USER
        private_key = file("exampleprivatekey)
        host = self.public_ip
    }
}

output "PublicIP" {
    value = aws_instance.test-inst.public_ip
}

output "PrivateIP" {
    value = aws_instance.test-inst.private_ip
}