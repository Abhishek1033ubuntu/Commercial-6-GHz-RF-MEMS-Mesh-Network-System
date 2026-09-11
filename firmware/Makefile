include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk

PKG_NAME:=mems-mesh-ctrl
PKG_RELEASE:=1

include $(INCLUDE_DIR)/package.mk

define KernelPackage/mems-mesh-ctrl
  SUBMENU:=Network Devices
  TITLE:=RF-MEMS Switch Cold-Switching Controller
  FILES:=$(PKG_BUILD_DIR)/mems_mesh_driver.ko
  AUTOLOAD:=$(call AutoProbe,mems_mesh_driver)
  DEPENDS:=+kmod-mac80211
endef

define KernelPackage/mems-mesh-ctrl/description
  Kernel module to execute sub-10us cold-switching for Menlo Micro MM5130/MM101 
  front-end on 6GHz mesh nodes, synchronized with 802.11ax TWT frame queues.
endef

MAKE_OPTS:= \
	ARCH="$(LINUX_KARCH)" \
	CROSS_COMPILE="$(TARGET_CROSS)" \
	M="$(PKG_BUILD_DIR)"

define Build/Compile
	$(MAKE) -C "$(LINUX_DIR)" $(MAKE_OPTS) modules
endef

$(eval $(call KernelPackage,mems-mesh-ctrl))
