#  Simulation-Based Inventory Optimization under Uncertainty

---

##  Problem Statement

Inventory decisions are critical in supply chain management, especially under uncertain demand and lead time conditions.

Traditional methods like EOQ fail to capture real-world variability.

This project builds a **simulation-based inventory system** to evaluate and optimize reorder policies under uncertainty.

---

##  Objective

- Model inventory behavior under demand variability  
- Incorporate lead time uncertainty  
- Evaluate system performance using simulation  
- Optimize Reorder Point (ROP)  
- Balance **cost vs service level**

---

##  Approach

- Simulated random demand using probability distribution  
- Modeled lead time delays  
- Implemented ROP-based inventory control logic  
- Ran **100+ simulations** for each policy  
- Evaluated performance using:

  -  Service Level  
  -  Stockouts  
  -  Total Cost  

---

##  Results

- Increasing ROP improves service level but increases cost  
- Lower ROP leads to frequent stockouts  
- Higher ROP ensures availability but increases holding cost  

 **Optimal Policy: ROP = 350 provides the best balance between cost and service level**

---

##  Key Insights

- Inventory systems must account for uncertainty  
- Simulation helps evaluate real-world scenarios  
- There is a clear **trade-off between cost and service level**  
- Data-driven decisions outperform static formulas  

---

##  Tools Used

- **Python** (NumPy, Pandas)  
- **Power BI** (Dashboard Visualization)


---
