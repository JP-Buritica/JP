# Grupo 12 - DANN Project

Proyecto para la asignatura **Desarrollo de Aplicaciones en la Nube (DANN)**.

## Team Members
- **m.hernandezg234@uniandes.edu.co** (Project Leader)
- **ma.quinteror1@uniandes.edu.co**
- **j.buriticar2@uniandes.edu.co**
- **jd.marinb1@uniandes.edu.co**

 
## Project Structure
```text
.
├── .github/workflows/    # CI/CD Pipelines
├── docs/                 # Documentation (Jekyll + PlantUML)
├── k8s/                  # Kubernetes Manifests
├── users_app/            # Microservice: Users
├── posts_app/            # Microservice: Posts
├── offers_app/           # Microservice: Offers
├── routes_app/           # Microservice: Routes
├── config.yaml           # Global Project Configuration
└── pyproject.toml        # Root dependency management (Poetry)
```

## Tech Stack
- **Language**: Python 3.11
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Environment**: Poetry
- **Infrastructure**: Docker & Kubernetes (Minikube)
- **CI/CD**: GitHub Actions

## Local Development Setup

### Prerequisites
- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation) (version 2.*)
- Minikube & kubectl

### Installation
1. Clone the repository.
2. Install dependencies for a specific microservice:
   ```bash
   make DIR=<app_folder> install # Assuming make target or manual poetry install
   ```

## Deploy to Minikube
1. Ensure Minikube is running: `minikube start`
2. Set up docker env: `& minikube -p minikube docker-env --shell powershell | Invoke-Expression`
3. Apply manifests:
   ```bash
   kubectl apply -f k8s/
   ```

## Testing
Run unit tests for any microservice with coverage reporting:
```bash
make unittest DIR=users_app
```

## Documentation
The documentation is built with Jekyll and deployed to GitHub Pages.
- **Local Preview**: `cd docs && bundle exec jekyll serve`
- **Documentation Link**: [GitHub Pages](https://misw-4301-desarrollo-apps-en-la-nube.github.io/202611-grupo12-proyecto/)

## CI/CD Pipelines
- `ci_evaluador_unit.yml`: Validates unit testing and coverage (>=70%).
- `ci_evaluador_entrega1_docs.yml`: Validates documentation (Vale + PlantUML).
- `ci_evaluador_entrega1_k8s.yml`: Validates K8s deployment and APIs.
