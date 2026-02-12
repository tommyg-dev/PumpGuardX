# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1-alpha] - 2026-02-12
### Added
- Official website and X (Twitter) community links to documentation.
- System detailed status endpoint to the backend API.

### Changed
- Refined wallet clustering algorithm docstrings and logging.
- Bumped system version across all core modules.

## [0.1.0-alpha] - 2026-02-11
### Added
- Initial release of the PumpGuardX Analysis Engine.
- Wallet clustering algorithm using Louvain Modularity.
- Statistical volume authenticity testing (Benford testing).
- React-based forensic dashboard with circular trust score visualization.
- FastAPI backend with modular analyzer architecture.
- Comprehensive documentation: Methodology, Architecture, and Whitepaper.

### Changed
- Reorganized repository structure for better root-level discoverability.
- Updated branding across all components.

### Fixed
- Improved SVG rendering on TrustScoreCard for mobile devices.
- Resolved race condition in concurrent data fetching simulation.
