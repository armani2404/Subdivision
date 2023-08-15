# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SubDivDialog
                                 A QGIS plugin
 This plugin partitions land parcels to smaller plots.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-09-15
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Caleb Amani
        email                : amanibaraka04@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'subdivision_dialog_base.ui'))


class SubDivDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SubDivDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.dsbLot_Width.setMinimum(15)
        self.dsbLot_Width.setDecimals(3)
        self.dsbLot_Width.setSuffix(" Metres")
        self.dsbLot_Length.setMinimum(30)
        self.dsbLot_Length.setDecimals(3)
        self.dsbLot_Length.setSuffix(" Metres")
        self.dsbRoad_Width.setSuffix(" Metres")