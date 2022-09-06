# Copyright (C) 2022 Canonical Ltd

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List, Dict, Union
from typing_extensions import Literal, TypedDict


TRequestMethods = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]

Toid = Union[str, int]


THeaders = Dict[str, str]

class TParams(TypedDict, total=False):
    ordering: List[str]
    page: int
    page_size: int
