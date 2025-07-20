
#include <linux/init.h>
#include <linux/module.h>
#include <linux/fs.h>

#define DEVICE_NAME "mychardev"

static int __init my_driver_init(void) {
    printk(KERN_INFO "Device loaded\n");
    return 0;
}

static void __exit my_driver_exit(void) {
    printk(KERN_INFO "Device unloaded\n");
}

module_init(my_driver_init);
module_exit(my_driver_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Test");
MODULE_DESCRIPTION("Sample Character Driver");
