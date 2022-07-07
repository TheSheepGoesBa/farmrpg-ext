/**
 * Return the card for a given cart title.
 * @param {Document} dom
 * @param {string | RegExp} title
 * @returns {Element?}
 */
export const findSection = (dom, title) => {
    const test = title instanceof RegExp ? val => title.test(val) : val => title === val
    for (const row of dom.querySelectorAll(".content-block-title")) {
        if (test(row.textContent.trim())) {
            return row.nextElementSibling
        }
    }
    return null
}

/**
 * Return the card title and element for all sections in a page.
 * @param {Document} dom
 * @returns {[string, Element][]}
 */
export const findAllSections = (dom) => {
    const sections = []
    for (const row of dom.querySelectorAll(".content-block-title")) {
        sections.push([row.textContent.trim(), row.nextElementSibling])
    }
    return sections
}

const numberRE = /^\s*([0-9,]+)/

/**
 * Parse out a number. Handles formats like "1,234" and "10x".
 * @param {string} str
 * @returns {number?}
 */
export const parseNumberString = (str) => {
    const match = str.match(numberRE)
    if (match) {
        return parseInt(match[1].replace(/,/g, ""), 10)
    } else {
        throw `Unable to parse number from ${str}`
    }
}
