# Created On: 2012/01/23
# Copyright 2012 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from .base import NoopGUI
from ..util import nonone

class TextField:
    def __init__(self, view=None):
        if view is None:
            view = NoopGUI()
        self.view = view
        self._text = ''
        self._value = None
    
    def _parse(self, text):
        return text
    
    def _format(self, value):
        return value
    
    def _update(self, newvalue):
        pass
    
    def refresh(self):
        self.view.refresh()
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, newtext):
        self.value = self._parse(nonone(newtext, ''))
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, newvalue):
        if newvalue == self._value:
            return
        self._value = newvalue
        self._text = self._format(newvalue)
        self._update(self._value)
        self.refresh()
    
