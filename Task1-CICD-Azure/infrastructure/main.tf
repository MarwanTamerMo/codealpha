# Terraform – Azure Infrastructure for Task 1 CI/CD Pipeline
# Provisions: Resource Group, ACR, App Service Plan, Web App

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.100"
    }
  }
  required_version = ">= 1.5"
}

provider "azurerm" {
  features {}
}

# ── Variables ─────────────────────────────────────────────────────────────────
variable "location" {
  description = "Azure region"
  default     = "East US"
}

variable "environment" {
  description = "Environment tag"
  default     = "production"
}

# ── Resource Group ────────────────────────────────────────────────────────────
resource "azurerm_resource_group" "rg" {
  name     = "codealpha-rg"
  location = var.location
  tags = {
    Project     = "CodeAlpha-DevOps-Internship"
    Task        = "Task1-CICD-Azure"
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# ── Azure Container Registry ──────────────────────────────────────────────────
resource "azurerm_container_registry" "acr" {
  name                = "codealphacr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
  tags                = azurerm_resource_group.rg.tags
}

# ── App Service Plan ──────────────────────────────────────────────────────────
resource "azurerm_service_plan" "asp" {
  name                = "codealpha-asp"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "B1"
  tags                = azurerm_resource_group.rg.tags
}

# ── Web App (container-based) ─────────────────────────────────────────────────
resource "azurerm_linux_web_app" "webapp" {
  name                = "codealpha-webapp"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.asp.id

  site_config {
    container_registry_use_managed_identity = false
    application_stack {
      docker_image_name        = "codealphacr.azurecr.io/webapp:latest"
      docker_registry_url      = "https://codealphacr.azurecr.io"
      docker_registry_username = azurerm_container_registry.acr.admin_username
      docker_registry_password = azurerm_container_registry.acr.admin_password
    }
    health_check_path = "/health"
  }

  app_settings = {
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = "false"
    ENVIRONMENT                         = "production"
  }

  tags = azurerm_resource_group.rg.tags
}

# ── Staging Slot ──────────────────────────────────────────────────────────────
resource "azurerm_linux_web_app_slot" "staging" {
  name           = "staging"
  app_service_id = azurerm_linux_web_app.webapp.id

  site_config {
    application_stack {
      docker_image_name        = "codealphacr.azurecr.io/webapp:latest"
      docker_registry_url      = "https://codealphacr.azurecr.io"
      docker_registry_username = azurerm_container_registry.acr.admin_username
      docker_registry_password = azurerm_container_registry.acr.admin_password
    }
    health_check_path = "/health"
  }

  app_settings = {
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = "false"
    ENVIRONMENT                         = "staging"
  }
}

# ── Outputs ───────────────────────────────────────────────────────────────────
output "webapp_url" {
  value       = "https://${azurerm_linux_web_app.webapp.default_hostname}"
  description = "Production web app URL"
}

output "acr_login_server" {
  value       = azurerm_container_registry.acr.login_server
  description = "ACR login server URL"
}

output "staging_url" {
  value       = "https://${azurerm_linux_web_app_slot.staging.default_hostname}"
  description = "Staging slot URL"
}
