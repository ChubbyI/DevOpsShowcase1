variable REGION {
    default = "us-east-2"
}

variable ZONE1 {
    default = "us-east-2a
}

variable AMIS {
    type = map
    defailt = {
        us-east-2 = "ami-03657b56516ab7912"
        us-east-1 = "ami-03657b56516ab7912"
    }
}

variable USER {
    default = "ec2-user"
}
