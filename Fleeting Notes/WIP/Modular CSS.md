Modular CSS is a way of organising your CSS to promotes **reusability**, and **consistency** while reducing **redundancy**. 

**Q?** - Why use Modular CSS?
**A!** - By adopting any of these modular CSS methodologies, developers can significantly enhance the maintainability, clarity, and scalability of their stylesheets. The advantages include:
1. **Ease of Maintenance**: modular css makes it easier to find and fix bugs, leading to reduced technical debt. 
2. **Scalability**: suitable for larger projects where designs may change frequently. 
3. **Team Collaboration**: provides a shared language among team members, making onboarding new developers more straightforward.
4. **Reusability**: encourages code reuse, reducing duplication and inconsistencies.

# Block Element Modifier (BEM)

BEM is a methodology aimed at creating reusable components and code sharing in front-end development. 
-  **Block**: represents the outermost element of a component. For example, in a card component, the card itself is the block. `card`
- **Element**: a part of a block that has no semantic meaning on its own. In a card, this could be the card's header or footer. `card__header`
- **Modifier**: A flag on a block of element. It used to change appearance or behaviour. Modifier can represent variations of a component. `card--featured`

# Scalable and Modular Architecture for CSS (SMACSS)

SMACSS is more concerned with the broader structure of your stylesheets rather than the precise naming of classes. SMACSS breaks down styles into five types:
1. **Base**: default styling for HTML element.
2. **Layout**: styles for structuring a page.
3. **Modular**: reusable and independent styles for UI components.
4. **State**: represents the different states of modules or layout components.
5. **Theme**: optional layer for altering the style of all components.

```css
/* Base */
p {
	font-size: 5px;
	line-height: 1.5;
}

/* Layout */
.l-container {
	max-width: 1200px; 
	margin: 0 auto;
}

/* Module */
.m-button {
	background-color: blue;
	color: white;
}

/* State */
.is-hidden {
	display: none;
}

/* Theme */
.t-dark {
	background-color: #333;
	color: #fff
}
```

# Object-Oriented CSS (OOCSS)

OOCSS is about separating structure (or containers) from skin (or the appearance) of objects. It encourages developers to think of components as objects, focusing on creating modular code that can be reused across a project.

<mark style="background: #BBFABBA6;">Key Principles</mark>:
- **Separate Structure and Skin**: separation of container styles from content styles.
- **Separate Containers and Content**: create reusable modules by applying multiple classes to an element.

```html
<div class="media">
	<img class="media__img" src="image.jpg">
	<div class="media__body">Object-Oriented CSS Concept</div>
</div>
```