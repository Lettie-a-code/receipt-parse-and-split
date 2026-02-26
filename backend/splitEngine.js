function equalSplit(totalDollars, people) {
	if (!Array.isArray(people) || people.length === 0) {
		throw new Error("people must be a non-empty array");
	}
	
	//convert dollars to cents
	const totalCents = Math.round(totalDollars * 100);
	
	const n = people.length;
	const base = Math.floor(totalCents / n);
	const remainder = totalCents % n;

	const result = {}

	//everyone is charged the base amount
	for (let i = 0; i < n; i++) {
		result[people[i]] = base;
	}

	//distribute the leftover cents
	for (let i = 0; i < remainder; i++) {
		result[people[i]] += 1;
	}
	
	//convert cents back to dollars for output
	const resultDollars= {};
	for (const person of people) {
		resultDollars[person] = (result[person] / 100).toFixed(2);
	}

	return resultDollars
}

module.exports = {
	equalSplit
};