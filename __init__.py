# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SubDiv
                                 A QGIS plugin
 This plugin partitions land parcels to smaller plots.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-09-15
        copyright            : (C) 2022 by Caleb Amani
        email                : amanibaraka04@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SubDiv class from file SubDiv.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .subdivision import SubDiv
    return SubDiv(iface)
