# Calculation of subbase drainage for the road pavement
#### Video Demo:  https://youtu.be/OL5igIVnEOs
#### Description:
I hold a degree as a certified engineering designer, specializing in the realm of road construction. When embarking on projects for highways, we rely on specific standards and calculation methodologies. The most critical component of a road is its pavement – the one that shoulders all vehicular loads. Accurate calculation of this pavement stands as a paramount task in road design.

Pavement design involves myriad factors influencing its durability and strength. Among these calculations is the drainage assessment for the underlying road base layer. This computation establishes the minimum allowable thickness of the road base layer, preventing structural oversaturation.

Existing software products like Indor and Robur inadequately conduct these calculations. Consequently, I've made the decision to create my own program that meticulously executes this calculation.

My program is coded in Python, employing the Flet framework to craft a graphical user interface. I've also utilized a fork of the simpledt library for table representation. Source data, tables, and calculation methodologies are gleaned from the normative document PNST 542-2021.

During the project's realization, I acquainted myself with the Flet framework. I mastered the art of importing and aptly presenting tables, seamlessly integrating them into the interface. I fashioned a foundational program interface that adapts fluidly to diverse screen resolutions or window sizes. I've also developed a program adept at filtering user inputs.

My program prompts users for a set of initial data. Some of this data is drawn from corresponding tables presented on the page. The source data is entered into appropriately named fields. The program necessitates numerical data in float format for calculation purposes. Additionally, the entered numbers must fall within predefined intervals. If incorrect data is entered and the "Calculate" button is pressed, an error message will display, indicating the necessary corrections.
