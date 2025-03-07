"""Plugin declaration for nautobot_golden_config."""

__version__ = "1.0.0-beta.1"

from nautobot.extras.plugins import PluginConfig


class GoldenConfig(PluginConfig):
    """Plugin configuration for the nautobot_golden_config plugin."""

    name = "nautobot_golden_config"
    verbose_name = "Golden Configuration"
    version = __version__
    author = "Network to Code, LLC"
    author_email = "opensource@networktocode.com"
    description = "A plugin for managing Golden Configurations."
    base_url = "golden-config"
    min_version = "1.2.0"
    max_version = "1.3.99"
    default_settings = {
        "enable_backup": True,
        "enable_compliance": True,
        "enable_intended": True,
        "enable_sotagg": True,
        "per_feature_bar_width": 0.3,
        "per_feature_width": 13,
        "per_feature_height": 4,
        "get_custom_compliance": None,
    }


config = GoldenConfig  # pylint:disable=invalid-name
