import sky

def vmStartAzure(cloud=sky.Azure() ,acc_type=None , n_cpus=None,n_memory=None , n_acc=None):

    task = sky.Task(run='echo hello world')
    task.set_resources(sky.Resources(cloud=cloud , accelerators={str(acc_type):n_acc} , memory=str(n_memory) , cpus=str(n_cpus)))

    sky.launch(task , down=True)