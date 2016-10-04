# coding=utf-8

# URL: https://pymedusa.com
#
# This file is part of Medusa.
#
# Medusa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Medusa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Medusa. If not, see <http://www.gnu.org/licenses/>.

"""Custom exceptions used or raised by indexer_api"""

# For backwards compatibility, can be removed and replaced with the default exception, when tvdb apiv1 is removed
from tvdb_api.tvdb_exceptions import tvdb_exception


class IndexerException(tvdb_exception):
    """Any exception generated by indexers api"""


class IndexerError(IndexerException):
    """An error with the indexers api (Cannot connect, for example)"""


class IndexerUserAbort(IndexerException):
    """User aborted the interactive selection (via the q command, ^c etc)"""


class IndexerShowNotFound(IndexerException):
    """Show cannot be found in the indexer (non-existant show)"""


class IndexerShowIncomplete(IndexerException):
    """Show found but incomplete in the indexer (incomplete show)"""


class IndexerSeasonNotFound(IndexerException):
    """Season cannot be found in the indexer"""


class IndexerEpisodeNotFound(IndexerException):
    """Episode cannot be found in the indexer"""


class IndexerAttributeNotFound(IndexerException):
    """Raised if an episode does not have the requested attribute (such as a episode name)"""
