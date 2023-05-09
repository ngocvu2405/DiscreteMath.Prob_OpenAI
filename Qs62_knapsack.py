#Với 1/0 knapsack => nhập giá trị 1 lần
#Multi knapsack => gấp số lần giá trị lên tầm 5 lần
#Nhập vào values, weights, capacities


from ortools.algorithms import pywrapknapsack_solver


def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    values = [
        10,5,3,6,10,5,3,6,10,5,3,6,10,5,3,6,
        10,5,3,6,10,5,3,6,10,5,3,6,10,5,3,6
    ]
    weights = [[
        5,3,2,4,5,3,2,4,5,3,2,4,5,3,2,4,
        5,3,2,4,5,3,2,4,5,3,2,4,5,3,2,4

    ]]
    capacities = [14]

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)


if __name__ == '__main__':
    main()