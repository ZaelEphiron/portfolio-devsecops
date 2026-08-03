# Pipeline CI/CD Sécurisé – GitHub Actions

Ce projet présente un pipeline CI/CD complet et sécurisé, conçu pour illustrer les bonnes pratiques DevSecOps.  
Il inclut des étapes de build, de tests, ainsi que plusieurs contrôles de sécurité automatisés.

## 🎯 Objectifs du pipeline

- Automatiser le build et les tests
- Intégrer des contrôles de sécurité (SAST, secrets scanning, dépendances)
- Démontrer une approche DevSecOps moderne
- Fournir un pipeline reproductible et extensible

## ⚙️ Outils utilisés

- GitHub Actions
- Semgrep (SAST)
- Gitleaks (scan de secrets)
- Trivy (scan de dépendances et conteneurs)
- Dependabot (analyse des dépendances)
- Actions de sécurité GitHub

## 🧩 Structure du pipeline

1. **Checkout du code**
2. **Installation des dépendances**
3. **Build**
4. **Tests unitaires**
5. **Scan SAST (Semgrep)**
6. **Scan de secrets (Gitleaks)**
7. **Scan de dépendances (Trivy)**
8. **Upload des artefacts**
9. **Badges de statut**

## 🔐 Sécurité du pipeline

- Permissions GitHub Actions minimales
- Secrets stockés dans GitHub Secrets
- Protection de la branche `main`
- Vérification des dépendances
- Scans automatisés à chaque push et pull request

## 📊 Diagramme du pipeline (Mermaid)

```mermaid
flowchart TD
    A[Push / PR] --> B[Checkout]
    B --> C[Build]
    C --> D[Tests]
    D --> E[SAST - Semgrep]
    D --> F[Scan Secrets - Gitleaks]
    D --> G[Scan Dépendances - Trivy]
    E --> H[Résultats]
    F --> H
    G --> H
    H --> I[Artefacts / Badges]
