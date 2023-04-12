-- Crea la DataBase
CREATE database IF NOT EXISTS JOB;

-- Elige la DataBases a usar
USE JOB;

show tables;

-- Crea tablas y relaciones
/* 
Tenemos una relación de uno a muchos entre Companies y Jobs, Locations y Jobs, y JobCategories y Jobs. 
Además, tenemos una relación de muchos a muchos entre Jobs y Skills, 
lo que significa que necesitamos una tabla de unión JobSkills.
*/
CREATE TABLE IF NOT EXISTS Companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS Locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    location_name VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS JobCategories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS Jobs (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    job_title VARCHAR(255),
    level VARCHAR(255),
    job_type VARCHAR(255),
    salary_range VARCHAR(255),
    benefits VARCHAR(255),
    onsite_remote VARCHAR(255),
    category_id INT,
    location_type VARCHAR(255),
    company_id INT,
    location_id INT,
    FOREIGN KEY (category_id) REFERENCES JobCategories(category_id),
    FOREIGN KEY (company_id) REFERENCES Companies(company_id),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS Skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS JobSkills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT,
    skill_id INT,
    FOREIGN KEY (category_id) REFERENCES JobCategories(category_id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


