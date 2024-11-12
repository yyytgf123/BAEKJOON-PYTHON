#vpc
resource "aws_vpc" "testVPC" {
	cidr_block = "10.0.0.0/16"
	enable_dns_hostnames = true
	tags = {
		Name="testVPC"
		}	
}

#subnet
#public subnet
resource "aws_subnet" "realPublicSubnet" {
	vpc_id = aws_vpc.testVPC.id
	cidr_block = "10.0.0.0/24"
	availability_zone = "ap-northeast-2c"
	tags = {
		Name = "real-public-subnet"
		}
}

#private subnet
resource "aws_subnet" "realPrivateSubnet1" {
	vpc_id = aws_vpc.testVPC.id
	cidr_block = "10.0.1.0/24"
	availability_zone = "ap-northeast-2c"
	tags = {
		Name = "real-private-subnet"
		}
}
resource "aws_subnet" "realPrivateSubnet2" {
	vpc_id = aws_vpc.testVPC.id
	cidr_block = "10.0.2.0/24"
	availability_zone = "ap-northeast-2a"
	tags = {
		Name = "real-private-subnet2"
		}
}

#IGW
resource "aws_internet_gateway" "realIGW" {
	vpc_id = aws_vpc.testVPC.id
	tags = {
		Name = "real-IGW"
		}
}

#routing table
#public routing table
resource "aws_route_table" "realPublicRoute" {
	vpc_id = aws_vpc.testVPC.id
	route {
		cidr_block = "0.0.0.0/0"
		gateway_id = aws_internet_gateway.realIGW.id
		}
	tags = {
		Name = "real-public-route"
		}
}
#private routing table
resource "aws_route_table" "realPrivateRoute" {
	vpc_id = aws_vpc.testVPC.id
	tags = {
		Name = "real-private-route"
		}
}
#public routing table connection
resource "aws_route_table_association" "realPublicRTAssociation" {
	subnet_id = aws_subnet.realPublicSubnet.id
	route_table_id = aws_route_table.realPublicRoute.id
}

#private routing table connection
resource "aws_route_table_association" "realPrivateRTAssociation1" {
	subnet_id = aws_subnet.realPrivateSubnet1.id
	route_table_id = aws_route_table.realPrivateRoute.id
}
resource "aws_route_table_association" "realPrivateRTAssociation2" {
	subnet_id = aws_subnet.realPrivateSubnet2.id
	route_table_id = aws_route_table.realPrivateRoute.id
}

#퍼블릭 보안 그룹
resource "aws_security_group" "realPublicSG" {
    vpc_id = aws_vpc.testVPC.id
    name = "real public SG"
    description = "real public SG"
    tags = {
        Name = "real pulbic SG"
    }
}
#퍼블릭 보안 그룹 규칙
resource "aws_security_group_rule" "realPublicSGRulesHTTPingress" {
    type = "ingress"
    from_port = 80
    to_port=80
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
    security_group_id = aws_security_group.realPublicSG.id
    lifecycle{
        create_before_destroy = true
    }
}
resource "aws_security_group_rule" "realPublicSGRulesSSHingress" {
    type = "ingress"
    from_port = 22
    to_port= 22
    protocol = "TCP"
    cidr_blocks=["0.0.0.0/0"]
    security_group_id = aws_security_group.realPublicSG.id
    lifecycle{
        create_before_destroy = true
    }
}
resource "aws_security_group_rule" "realPublicSGRulesALLegress" {
    type = "egress"
    from_port = 0
    to_port= 0
    protocol = "ALL"
    cidr_blocks=["0.0.0.0/0"]
    security_group_id = aws_security_group.realPublicSG.id
    lifecycle{
        create_before_destroy = true
    }
}
#프라이빗 보안 그룹
#주로DB연결 과 같은 외부의 접근을 허용하지 않는 포트 번호를 가짐
resource "aws_security_group" "realPrivateSG" {
    vpc_id = aws_vpc.testVPC.id
    name = "real private SG"
    description = "real private SG"
    tags = {
        Name = "real private SG"
    }
}
#프라이빗 보안 그룹 규칙
resource "aws_security_group_rule" "realPrivateSGRulesRDSingress" {
    type = "ingress"
    from_port = 3306
    to_port=3306
    protocol = "TCP"
    security_group_id = aws_security_group.realPrivateSG.id
    source_security_group_id = aws_security_group.realPublicSG.id
    lifecycle{
        create_before_destroy = true
    }
}
resource "aws_security_group_rule" "realPrivateSGRulesRDSegress" {
    type = "egress"
    from_port = 3306
    to_port= 3306
    protocol = "TCP"
    security_group_id = aws_security_group.realPrivateSG.id
    source_security_group_id = aws_security_group.realPublicSG.id
    lifecycle{
        create_before_destroy = true
    }
}