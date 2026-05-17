"""
IBM watsonx Orchestrate Engine for SmartLaunch AI
==================================================
This module simulates a multi-agent workflow orchestration system that processes
repository analysis through sequential AI skills. Each skill represents a specialized
agent that performs a specific task in the onboarding pipeline.

Author: SmartLaunch AI Team
Version: 1.0.0
"""

import time
import json
from typing import List, Dict, Generator, Any


class WatsonxOrchestrator:
    """
    Orchestrates multi-agent workflows for automated repository onboarding.
    
    This class simulates the IBM watsonx Orchestrate platform by coordinating
    multiple AI skills in a sequential pipeline. Each skill processes repository
    data and yields real-time progress updates for UI integration.
    """
    
    def __init__(self):
        """Initialize the orchestrator with default configuration."""
        self.skill_delay = 0.8  # Simulated processing time per skill (seconds)
        self.workflow_version = "1.0.0"
        
    def run_onboarding_workflow(
        self, 
        file_list: List[str], 
        tech_stack: str
    ) -> Generator[Dict[str, Any], None, None]:
        """
        Execute the complete onboarding workflow through orchestrated AI skills.
        
        This method yields progress updates as each skill completes, allowing
        the UI to display live status updates. The workflow consists of three
        sequential skills that analyze and process repository data.
        
        Args:
            file_list (List[str]): List of file paths from the uploaded repository
            tech_stack (str): Detected technology stack (e.g., "Python 🐍", "Node.js 🟢")
            
        Yields:
            Dict[str, Any]: Progress update containing:
                - skill_name (str): Name of the current skill
                - status (str): "processing" or "completed"
                - progress (int): Percentage complete (0-100)
                - data (Dict): Skill-specific output data
                
        Example:
            >>> orchestrator = WatsonxOrchestrator()
            >>> for update in orchestrator.run_onboarding_workflow(files, "Python 🐍"):
            ...     print(f"Skill: {update['skill_name']}, Status: {update['status']}")
        """
        
        # Skill 1: Repository Structure Mapping
        yield self._execute_skill_1(file_list, tech_stack)
        
        # Skill 2: Security & Configuration Audit
        yield self._execute_skill_2(file_list, tech_stack)
        
        # Skill 3: Onboarding Asset Generation
        yield self._execute_skill_3(file_list, tech_stack)
    
    def _execute_skill_1(
        self, 
        file_list: List[str], 
        tech_stack: str
    ) -> Dict[str, Any]:
        """
        Skill 1: Repository Structure Mapping
        
        Analyzes the repository file structure and creates a visual tree overview.
        This skill identifies key directories, file types, and organizational patterns
        to help developers understand the project layout quickly.
        
        Args:
            file_list (List[str]): List of file paths from repository
            tech_stack (str): Detected technology stack
            
        Returns:
            Dict[str, Any]: Structured output containing:
                - skill_name: Identifier for this skill
                - status: Completion status
                - progress: Percentage complete
                - data: Skill-specific results including file tree and statistics
        """
        # Simulate AI processing time
        time.sleep(self.skill_delay)
        
        # Analyze repository structure
        directories = set()
        file_extensions = {}
        
        for file_path in file_list:
            # Extract directory structure
            parts = file_path.split('/')
            if len(parts) > 1:
                directories.add(parts[0])
            
            # Count file extensions
            if '.' in file_path:
                ext = file_path.split('.')[-1]
                file_extensions[ext] = file_extensions.get(ext, 0) + 1
        
        # Generate visual tree structure
        tree_structure = self._generate_tree_view(file_list)
        
        # Compile skill output
        skill_output = {
            "skill_name": "Repository Structure Mapping",
            "status": "completed",
            "progress": 33,
            "data": {
                "total_files": len(file_list),
                "total_directories": len(directories),
                "top_directories": sorted(list(directories))[:10],
                "file_type_distribution": file_extensions,
                "tree_preview": tree_structure[:15],  # First 15 lines of tree
                "tech_stack": tech_stack,
                "complexity_score": self._calculate_complexity(file_list),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }
        
        return skill_output
    
    def _execute_skill_2(
        self, 
        file_list: List[str], 
        tech_stack: str
    ) -> Dict[str, Any]:
        """
        Skill 2: Security & Configuration Audit
        
        Performs a comprehensive security scan to identify potential vulnerabilities,
        missing configuration files, and exposed sensitive data. This skill helps
        ensure the repository follows security best practices.
        
        Args:
            file_list (List[str]): List of file paths from repository
            tech_stack (str): Detected technology stack
            
        Returns:
            Dict[str, Any]: Structured output containing:
                - skill_name: Identifier for this skill
                - status: Completion status
                - progress: Percentage complete
                - data: Security audit results and recommendations
        """
        # Simulate AI processing time
        time.sleep(self.skill_delay)
        
        # Security audit checks
        has_env_file = any('.env' in f for f in file_list)
        has_gitignore = any('.gitignore' in f for f in file_list)
        has_readme = any('README' in f.upper() for f in file_list)
        has_license = any('LICENSE' in f.upper() for f in file_list)
        
        # Check for potential security risks
        security_risks = []
        if not has_env_file:
            security_risks.append({
                "severity": "medium",
                "issue": "Missing .env file",
                "recommendation": "Create a .env file for environment variables"
            })
        
        if not has_gitignore:
            security_risks.append({
                "severity": "high",
                "issue": "Missing .gitignore file",
                "recommendation": "Add .gitignore to prevent committing sensitive files"
            })
        
        # Check for exposed keys (simplified pattern matching)
        exposed_keys = self._scan_for_exposed_keys(file_list)
        
        # Calculate security score
        security_score = 100
        security_score -= len(security_risks) * 15
        security_score -= len(exposed_keys) * 25
        security_score = max(0, security_score)
        
        # Compile skill output
        skill_output = {
            "skill_name": "Security & Configuration Audit",
            "status": "completed",
            "progress": 66,
            "data": {
                "security_score": security_score,
                "has_env_file": has_env_file,
                "has_gitignore": has_gitignore,
                "has_readme": has_readme,
                "has_license": has_license,
                "security_risks": security_risks,
                "exposed_keys_count": len(exposed_keys),
                "exposed_keys_files": exposed_keys,
                "recommendations": self._generate_security_recommendations(
                    has_env_file, has_gitignore, has_readme, has_license
                ),
                "compliance_status": "PASS" if security_score >= 70 else "NEEDS_ATTENTION",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }
        
        return skill_output
    
    def _execute_skill_3(
        self, 
        file_list: List[str], 
        tech_stack: str
    ) -> Dict[str, Any]:
        """
        Skill 3: Onboarding Asset Generation
        
        Generates comprehensive onboarding materials including terminal commands,
        setup instructions, and custom tracking tickets. This skill creates
        actionable documentation to accelerate developer onboarding.
        
        Args:
            file_list (List[str]): List of file paths from repository
            tech_stack (str): Detected technology stack
            
        Returns:
            Dict[str, Any]: Structured output containing:
                - skill_name: Identifier for this skill
                - status: Completion status
                - progress: Percentage complete
                - data: Generated onboarding assets and tracking tickets
        """
        # Simulate AI processing time
        time.sleep(self.skill_delay)
        
        # Generate terminal commands based on tech stack
        terminal_commands = self._generate_terminal_commands(tech_stack, file_list)
        
        # Create tracking tickets for onboarding tasks
        tracking_tickets = self._generate_tracking_tickets(tech_stack, file_list)
        
        # Generate setup documentation
        setup_guide = self._generate_setup_guide(tech_stack, file_list)
        
        # Compile skill output
        skill_output = {
            "skill_name": "Onboarding Asset Generation",
            "status": "completed",
            "progress": 100,
            "data": {
                "terminal_commands": terminal_commands,
                "tracking_tickets": tracking_tickets,
                "setup_guide": setup_guide,
                "estimated_setup_time": self._estimate_setup_time(tech_stack),
                "prerequisite_tools": self._get_prerequisite_tools(tech_stack),
                "quick_start_steps": self._generate_quick_start(tech_stack),
                "troubleshooting_tips": self._generate_troubleshooting_tips(tech_stack),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }
        
        return skill_output
    
    # ==================== Helper Methods ====================
    
    def _generate_tree_view(self, file_list: List[str]) -> List[str]:
        """Generate a visual tree structure from file paths."""
        tree = []
        for file_path in sorted(file_list)[:15]:  # Limit to first 15 files
            depth = file_path.count('/')
            indent = "  " * depth
            filename = file_path.split('/')[-1]
            tree.append(f"{indent}├── {filename}")
        return tree
    
    def _calculate_complexity(self, file_list: List[str]) -> str:
        """Calculate project complexity based on file count and structure."""
        file_count = len(file_list)
        if file_count < 10:
            return "Low"
        elif file_count < 50:
            return "Medium"
        else:
            return "High"
    
    def _scan_for_exposed_keys(self, file_list: List[str]) -> List[str]:
        """Scan for files that might contain exposed API keys or secrets."""
        suspicious_files = []
        sensitive_patterns = ['config', 'secret', 'key', 'token', 'password', 'credential']
        
        for file_path in file_list:
            filename_lower = file_path.lower()
            if any(pattern in filename_lower for pattern in sensitive_patterns):
                if not file_path.endswith('.gitignore') and '.env' not in file_path:
                    suspicious_files.append(file_path)
        
        return suspicious_files
    
    def _generate_security_recommendations(
        self, 
        has_env: bool, 
        has_gitignore: bool, 
        has_readme: bool, 
        has_license: bool
    ) -> List[str]:
        """Generate security recommendations based on audit results."""
        recommendations = []
        
        if not has_env:
            recommendations.append("Create a .env file for environment-specific configuration")
        if not has_gitignore:
            recommendations.append("Add a .gitignore file to exclude sensitive files from version control")
        if not has_readme:
            recommendations.append("Add a README.md file to document the project")
        if not has_license:
            recommendations.append("Consider adding a LICENSE file to clarify usage rights")
        
        recommendations.append("Review all configuration files for hardcoded credentials")
        recommendations.append("Enable branch protection rules in your repository settings")
        
        return recommendations
    
    def _generate_terminal_commands(self, tech_stack: str, file_list: List[str]) -> List[Dict[str, str]]:
        """Generate terminal commands based on detected tech stack."""
        commands = []
        
        if "Python" in tech_stack:
            commands = [
                {"step": "1", "command": "python -m venv venv", "description": "Create virtual environment"},
                {"step": "2", "command": "source venv/bin/activate", "description": "Activate virtual environment (Unix)"},
                {"step": "3", "command": "pip install -r requirements.txt", "description": "Install dependencies"},
                {"step": "4", "command": "python app.py", "description": "Run the application"}
            ]
        elif "Node.js" in tech_stack:
            commands = [
                {"step": "1", "command": "npm install", "description": "Install dependencies"},
                {"step": "2", "command": "npm run dev", "description": "Start development server"},
                {"step": "3", "command": "npm test", "description": "Run test suite"}
            ]
        else:
            commands = [
                {"step": "1", "command": "# Review project documentation", "description": "Check README for setup instructions"}
            ]
        
        return commands
    
    def _generate_tracking_tickets(self, tech_stack: str, file_list: List[str]) -> List[Dict[str, str]]:
        """Generate tracking tickets for onboarding tasks."""
        tickets = [
            {
                "id": "ONBOARD-001",
                "title": "Environment Setup",
                "description": "Configure local development environment",
                "priority": "High",
                "status": "Pending"
            },
            {
                "id": "ONBOARD-002",
                "title": "Dependency Installation",
                "description": "Install all required project dependencies",
                "priority": "High",
                "status": "Pending"
            },
            {
                "id": "ONBOARD-003",
                "title": "Configuration Review",
                "description": "Review and update configuration files",
                "priority": "Medium",
                "status": "Pending"
            },
            {
                "id": "ONBOARD-004",
                "title": "Initial Test Run",
                "description": "Execute application and verify functionality",
                "priority": "Medium",
                "status": "Pending"
            }
        ]
        
        return tickets
    
    def _generate_setup_guide(self, tech_stack: str, file_list: List[str]) -> str:
        """Generate a comprehensive setup guide."""
        guide = f"""
# Setup Guide for {tech_stack} Project

## Prerequisites
- Ensure you have the required tools installed (see prerequisite_tools)
- Clone the repository to your local machine
- Navigate to the project directory

## Quick Start
1. Review the project structure and documentation
2. Install dependencies using the provided commands
3. Configure environment variables if needed
4. Run the application and verify it works

## Next Steps
- Explore the codebase and understand the architecture
- Review any existing documentation
- Set up your development workflow
- Connect with the team for any questions
"""
        return guide.strip()
    
    def _estimate_setup_time(self, tech_stack: str) -> str:
        """Estimate the time required for complete setup."""
        if "Python" in tech_stack:
            return "15-20 minutes"
        elif "Node.js" in tech_stack:
            return "10-15 minutes"
        else:
            return "20-30 minutes"
    
    def _get_prerequisite_tools(self, tech_stack: str) -> List[str]:
        """Get list of prerequisite tools based on tech stack."""
        if "Python" in tech_stack:
            return ["Python 3.8+", "pip", "virtualenv", "Git"]
        elif "Node.js" in tech_stack:
            return ["Node.js 14+", "npm or yarn", "Git"]
        else:
            return ["Git", "Text Editor/IDE"]
    
    def _generate_quick_start(self, tech_stack: str) -> List[str]:
        """Generate quick start steps."""
        return [
            "Clone the repository",
            "Install dependencies",
            "Configure environment variables",
            "Run the application",
            "Verify functionality"
        ]
    
    def _generate_troubleshooting_tips(self, tech_stack: str) -> List[Dict[str, str]]:
        """Generate troubleshooting tips for common issues."""
        tips = [
            {
                "issue": "Dependency installation fails",
                "solution": "Check your internet connection and package manager version"
            },
            {
                "issue": "Application won't start",
                "solution": "Verify all environment variables are set correctly"
            },
            {
                "issue": "Port already in use",
                "solution": "Change the port number in configuration or stop conflicting services"
            }
        ]
        
        return tips


# ==================== Module-Level Functions ====================

def create_orchestrator() -> WatsonxOrchestrator:
    """
    Factory function to create a new WatsonxOrchestrator instance.
    
    Returns:
        WatsonxOrchestrator: A new orchestrator instance ready for workflow execution
        
    Example:
        >>> orchestrator = create_orchestrator()
        >>> for update in orchestrator.run_onboarding_workflow(files, stack):
        ...     print(update)
    """
    return WatsonxOrchestrator()


def get_workflow_info() -> Dict[str, Any]:
    """
    Get information about the orchestration workflow.
    
    Returns:
        Dict[str, Any]: Workflow metadata including version and skill count
    """
    return {
        "version": "1.0.0",
        "skill_count": 3,
        "platform": "IBM watsonx Orchestrate (Simulated)",
        "description": "Multi-agent workflow for automated repository onboarding"
    }

# Made with Bob
