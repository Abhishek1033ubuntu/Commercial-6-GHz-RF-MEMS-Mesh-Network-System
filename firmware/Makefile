include $(TOPDIR)/rules.mk

PKG_NAME:=kmod-mems-mesh-ctrl
PKG_RELEASE:=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/kernel.mk

define KernelPackage/mems-mesh-ctrl
  SUBMENU:=Network Devices
  TITLE:=Menlo Micro RF-MEMS Switch Controller
  FILES:=$(PKG_BUILD_DIR)/mems_mesh_driver.ko
  AUTOLOAD:=$(call AutoProbe,mems_mesh_driver)
endef

define Build/Compile
	$(MAKE) -C "$(LINUX_DIR)" \
		KERNEL_DIR="$(LINUX_DIR)" \
		M="$(PKG_BUILD_DIR)" \
		modules
endef

$(eval $(call KernelPackage,mems_mesh_ctrl))
