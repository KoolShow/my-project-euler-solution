fn gen_prime(primes: &Vec<i32>, max: Option<i32>) -> Vec<i32> {
    let mut new_primes = Vec::new();
    let last_prime = *primes.last().unwrap();
    let max_n = match max {
        Some(n) => n,
        None => match last_prime.checked_mul(last_prime) {
            Some(n) => n,
            None => i32::MAX,
        },
    };
    for n in (last_prime+2..max_n).step_by(2) {
        if primes.iter().all(|&p| n % p != 0) {
            new_primes.push(n);
        }
    }
    new_primes
}


fn main() {
    let mut primes = vec![3, 5, 7, 11, 13, 17, 19];
    primes.extend(gen_prime(&primes, None));
    primes.extend(gen_prime(&primes, None));
    primes.extend(gen_prime(&primes, Some(2000000i32)));

    let sum: i64 = primes.iter().map(|&x| x as i64).sum();
    println!("Ans = {}", sum+2);
}
