cmake_minimum_required(VERSION 3.13.4)

project(SlicerCASTutorial)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCASTutorial")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "Junichi Tokuda (Brigham and Women's Hosiptal)")
set(EXTENSION_DESCRIPTION "This is a module for Slicer for CAS tutorial.")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/SlicerCASTutorial.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/SlicerCASTutorial/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(ProximityWarning)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
