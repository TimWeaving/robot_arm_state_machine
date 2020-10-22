

def joint_0_function(x,y,z):
    # do some function to transfer movement of joint into movement in global axis
    # depends on oriention of all other joints so not sure how this is done off the top of my head
    x_dash,y_dash,z_dash = x,y,z
    return x_dash,y_dash,z_dash

def joint_1(x,y,z):
    # do some function to transfer movement of joint into movement in global axis
    # depends on oriention of all other joints so not sure how this is done off the top of my head
    x_dash1,y_dash1,z_dash1 = joint_0_function(x,y,z)
    x_dash2,y_dash2,z_dash2 = x_dash1,y_dash1,z_dash1

    return x_dash2,y_dash2,z_dash2