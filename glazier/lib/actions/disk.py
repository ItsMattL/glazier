# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Actions to manipulate the disk."""

from glazier.lib import disk
from glazier.lib.actions.base import ActionError
from glazier.lib.actions.base import BaseAction


class WriteDiskSpace(BaseAction):
  """Writes the current total, used, and free disk space to registry."""

  def Run(self):
    try:
      disk.set_disk_space()
    except disk.Error as e:
      raise ActionError(e)
